from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


# Create your views here.
def gethome(request):

    products = Product.objects.all()  # Fetch all products from the database
    categories = products.values_list('category', flat=True).distinct() #loại hàng
    origins = products.values_list('origin', flat=True).distinct() #xuất xứ

    #Filter products
    category = request.GET.get('category')
    origin = request.GET.get('origin')
    price_range = request.GET.get('price_range')

    if category and category != 'all':
        products = products.filter(category=category)
    if origin and origin != 'all':
        products = products.filter(origin=origin)
    if price_range and price_range != 'all':
        if price_range.startswith('>'):
            min_price = int(price_range[1:])
            products = products.filter(price__gt=min_price)
        else:
            min_price, max_price = map(int, price_range.split('-'))
            products = products.filter(price__gte=min_price, price__lte=max_price)  

    # Pagination
    paginator = Paginator(products, 6)  # Show 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj, 'categories': categories, 'origins': origins})
   
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

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm