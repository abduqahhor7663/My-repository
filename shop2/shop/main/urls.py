from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("cart/", views.cartdetail, name="cart"),
    path("detail/<slug:slug>", views.ProductDetailView.as_view(), name="detail"),
    path("about/", views.about, name="about"),
]