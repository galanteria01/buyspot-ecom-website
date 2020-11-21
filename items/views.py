from django.shortcuts import render
from .models import Item
# Create your views here.

def show_all(request):
    items = Item.objects.all().order_by('date')
    return render(request,'items/show_items.html',{'items':items})

def show_item(request,slug):
    item = Item.objects.get(slug=slug)
    return render(request,'items/single_item.html',{'item',item})