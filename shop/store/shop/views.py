from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = "index.html"

# class CartView(DetailView):
#     model = Product
#     template_name = "cart.html"
    
def cartdetail(request):
    
    return render(request,"cart.html")