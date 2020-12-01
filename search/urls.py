from django.shortcuts import redirect,render
from django.urls import path,include
from . import views

app_name = "search"

urlpatterns =[
    path('',views.search_result,name="search_result")
]