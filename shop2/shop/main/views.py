from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context
    
def products(request):
    products = Product.objects.all()
    brands = Brand.object.all()
    return render(request, {'cat':categories})
    
    
    
def cartdetail(request):
    product_id = request.GET.get('product_id')
    
    return render(request,"cart.html", {'product_id': product_id})
    


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context
    


def about(request):
    
    return render(request,"about.html")


def category_detail(request, slug):
    product = Product.objects.filter(category__slug=slug)
    # items = Item.objects.filter(category=category)
    cat = Category.objects.all()
    brand = Brand.objects.all()
    return render(request, 'category_detail.html', {'products': product, 'categories':cat, 'brands': brand,})


def brand_detail(request, slug):
    product = Product.objects.filter(brand__slug=slug)
    # items = Item.objects.filter(category=category)
    brand = Brand.objects.all()
    cat = Category.objects.all()
    return render(request, 'brand_detail.html', {'products': product, 'brands':brand, 'categories': cat,})

