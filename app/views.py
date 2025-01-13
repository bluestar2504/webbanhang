from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
import mysql.connector


# Create your views here.
def gethome(request):
    results = []
    query = request.GET.get('query', '')  # Lấy từ khóa tìm kiếm từ query string
    if query:
        results = perform_search(query)  # Thực hiện tìm kiếm nếu có từ khóa
    return render(request, 'index.html', {'results': results, 'query': query})  # Trả về kết quả tìm kiếm

def getdetail(request):
    return render(request,'product_detail.html')
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