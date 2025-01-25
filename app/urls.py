from django.contrib import admin
from django.urls import path
from app import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('',views.gethome,name='home'),
    path('product/<int:product_id>/', views.getdetail, name='product_detail'),
    path('cart/',views.getcart),
    path('checkout/',views.getcheckout),
    path('test/',views.gettest),

]
