from django.urls import path
from . import views
app_name = 'items'

urlpatterns = [
    path('',views.show_all,name='list'),
    path('<slug:slug>',views.show_item,name='details'),
]   