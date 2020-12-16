from django.urls import path
from . import views

app_name = "shopping_cart"

urlpatterns = [ 
    path("add_to_cart/<int:item_id>",views.add_to_cart,name="add_to_cart"),
    path("order_summary",views.order_summary,name="order_summary"), 
    path("remove_from_cart/<int:item_id>",views.delete_from_cart,name="remove_from_cart"),
    path("success",views.success,name="purchase_success"),
    path("checkout",views.checkout,name="checkout"),
    path("update_transaction/<int:token>",views.update_transactions_records,name="update_records"),

]