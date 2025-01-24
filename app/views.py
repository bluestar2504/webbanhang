from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employee,Product
import mysql.connector


# Create your views here.
def gethome(request):
    results = []
    query = request.GET.get('query', '')  # Lấy từ khóa tìm kiếm từ query string
    if query:
        results = perform_search(query)  # Thực hiện tìm kiếm nếu có từ khóa
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'index.html', {'results': results, 'query': query, 'products': products}) #tra ve index 

def getdetail(request,product_id):
    product = get_object_or_404(Product, product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})
def gettest(request):
    return render(request,'app1/test.html')
def getcart(request):
    context={}
    return render(request,'cart.html',context)
def getcheckout(request):
    context={}
    return render(request,'checkout.html',context)




def perform_search(query):
    return Employee.objects.filter(first_name__icontains=query)  # Tìm kiếm nhân viên theo tên