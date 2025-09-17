from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("cart/", views.cartdetail, name="cart"),
    path("detail/<slug:slug>", views.ProductDetailView.as_view(), name="detail"),
    path("about/", views.about, name="about"),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('brand/<slug:slug>/', views.brand_detail, name='brand_detail'),
]

