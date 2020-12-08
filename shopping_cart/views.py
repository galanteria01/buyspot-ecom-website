
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from items.models import Item
from .models import orderItem, Order,Transaction
from .extras import generate_order_id
from ecommerce import settings
import datetime
import stripe
from .extras import*

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile,user=request.user)
    item = Item.objects.filter(itemID=kwargs.get('item_id',"")).first()
    if item in request.user.profile.items.all():
        messages.info(request,"You already have this product")
        return render(request,"order_summary.html")
    order_item,status = orderItem.objects.get_or_create(product=item)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.add_message(request,messages.INFO,"Item added to cart")
    return redirect(reverse('items:list'))

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = orderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))

def order_summary(request,**kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order':existing_order
    }
    return render(request,'shopping_cart/order_summary.html',context)


@login_required
def checkout(request,**kwargs):
    client_token = generate_client_token()
    existing_order = get_user_pending_order(request)
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST.get('stripeToken',False)
        if token:
            try:
                charge = stripe.Charge.create(
                    amount = 100*existing_order.get_cart_total(),
                    current='inr',
                    description="Example charge",
                    source=token,
                )
                return redirect(reverse('shopping_cart:update_records',kwargs={'token':token}))
            except Exception as e:
                messages.info(request,"Your card has been declined,{e}")
            
        else:
            result = transact({
                'amount':existing_order.get_cart_total(),
                'payment_method_nonce':request.POST['payment_method_nonce'],
                'options':{"submit_for_settlement":True}
            })
            if result.is_success or result.transaction:
                return redirect(reverse('shopping_cart:update_records',kwargs={'token': result.transaction.id}))
            else:
                for x in result.errors.deep_errors:
                    messages.info(request,x)
                return redirect(reverse('shopping_cart:checkout'))
        context = {
            'order':existing_order,
            'client_token':client_token,
            "STRIPE_PUBLISHABLE_KEY":publishKey
        }
        return render(request,'shopping_cart/checkout.html',context)

@login_required
def update_transactions_records(request,token):
    order_to_purchase = get_user_pending_order(request)
    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered=True,date_ordered=datetime.datetime.now())

    user_profile = get_object_or_404(Profile,user=request.user)
    order_products = [item.product for item in order_items]
    user_profile.items.add(*order_products)
    user_profile.save()

    transaction = Transaction(profile=request.user.profile,
                            token=token,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)
    transaction.save()

    messages.info(request,"Thank you! Purchase is successful")
    return redirect(reverse('accounts:user_details'))



def success(request, **kwargs):
    # a view signifying the transaction was successful
    return render(request, 'shopping_cart/purchase_success.html', {})