from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup',views.signup_view,name="signup"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('user',views.user_details,name="user"),
    path('sent', views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]