from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = "index.html"
    
def products(request):
    products = Product.objects.all()
    cat = Category.object.all()
    brands = Brand.object.all()
    return render(request, {'cat':categories})
    
def cartdetail(request):
    
    return render(request,"cart.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"


def about(request):
    
    return render(request,"about.html")