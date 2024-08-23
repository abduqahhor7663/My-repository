from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    
    
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name


COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
    ('white', 'White'),
]

class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_products")
    color = models.CharField(max_length=10, choices=COLORS)
    rating = models.FloatField(blank=True)
    cell_count = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.PositiveSmallIntegerField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    aviable = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name

    def get_discount_price(self):
        price = self.price
        discount = self.discount
        if discount:
            return price - (price * discount / 100)
        else:
            return price

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_ratings")
    rating = models.FloatField()
    value = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


