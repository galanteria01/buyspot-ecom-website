from django.shortcuts import render
from .models import Item
# Create your views here.

def show_all(request):
    items = Item.objects.all().order_by('date')
    return render(request,'items/show_items.html',{'items':items})