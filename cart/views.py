from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request,shoeDetails):
    return


def remove_from_cart(request):
    return

def viewCart(request):
    return