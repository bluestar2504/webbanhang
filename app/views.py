from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gethome(request):
    return render(request,'index.html')
def getdetail(request):
    return render(request,'product_detail.html')
def gettest(request):
    return render(request,'app1/test.html')