from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gethome,name='home'),
    path('detail/',views.getdetail),
    path('cart/',views.getcart),
    path('checkout/',views.getcheckout),
    path('test/',views.gettest),


]
