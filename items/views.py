from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from shopping_cart.models import Order


# Create your views here.

def show_homepage(request):
    return render(request,'items/homepage.html')

def show_all(request):
    items = Item.objects.all().order_by('date')
    current_order_products = []

    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]
    context = {
        'items': items,
        'current_order_products': current_order_products
    }
    return render(request, 'items/show_items.html', context)


def show_item(request, slug):
    item = Item.objects.get(slug=slug)
    return render(request, 'items/single_item.html', {'item': item})
