from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gethome,name='home'),
    path('product/<int:product_id>/', views.getdetail, name='product_detail'),
    path('cart/',views.getcart),
    path('checkout/',views.getcheckout),
    path('test/',views.gettest),

]
