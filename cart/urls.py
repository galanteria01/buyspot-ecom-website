from django.urls import path,include
from . import views

app_name = 'cart'

urlpatterns = [
    path('add_to_cart',views.add_to_cart,name="addCart"),
    path('remove_from_cart',views.remove_from_cart,name="removeCart"),
    path('view_cart',views.view_cart,name="viewCart")

]