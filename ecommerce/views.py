from django.shortcuts import render,redirect

def show_home(request):
    return redirect('items:home')

def show_deals(request):
    return redirect('items:list')

