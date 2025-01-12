from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gethome),
    path('detail/',views.getdetail),
    path('test/',views.gettest)
]
