
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from items.models import Item
from .models import orderItem, Order
from .extras import generate_order_id

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
    item = Item.objects.filter(id=kwargs.get('item_id',"")).first()
    if item in request.user.profile.items.all():
        messages.info(request,"You already have this product")
        return redirect('items:list')
    order_item,status = OrderItem.objects.get_or_create(product=item)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect('items:list')

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
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