from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Cart
from items.models import Item
# Create your views here.

@login_required
def add_to_cart(request):
    #item = get_object_or_404(Item, pk=itemID)
    #cart,created = Item.objects.get_or_create(user=request.user, active=True)
    
    messages.success(request, "Cart updated!")
    return render(request,'cart/view_cart.html')


def remove_from_cart(request):
    return render(request,'cart/view_cart.html')
def view_cart(request):
    return render(request,'cart/view_cart.html')