from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('items.list')
    elif request.method == "GET":
        form = UserCreationForm()
    return render(request,'accounts/signup_page.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('items:list')
    elif request.method == "GET":
        form  = AuthenticationForm()
    return render(request,'accounts/login_page.html',{'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('items:list')