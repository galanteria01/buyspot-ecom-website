"""ecommerce URL Configuration

"""
from django.contrib import admin   
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.conf.urls.static import static

app_name = "ecommerce"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show_home,name="home"),
    path('deals/',views.show_deals,name="deals"),
    path('search/',include('search.urls')),
    path('items/',include('items.urls')),
    path('accounts/',include('accounts.urls')),
    #path('transactions/',include('transactions.urls')),
    path('shopping_cart/',include('shopping_cart.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)