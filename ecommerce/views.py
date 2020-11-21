from django.shortcuts import render

def show_home(request):
    return render(request,'base_layout.html')