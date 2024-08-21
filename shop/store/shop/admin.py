# from django.contrib import admin
# from .models import Brand,Product,Rating,Category,SubCategory
# # Register your models here.
# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}
    
    
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name',"stock","aviable","price",]
#     list_display_links = ("name",)
#     list_editable = ["price","stock","aviable" ]
#     search_fields = ['name']
#     prepopulated_fields = {'slug':('name',)}

# # @admin.register(SubCategory)
# # class SubCategoryAdmin(admin.ModelAdmin):
# #     list_display = ['name','slug']
# #     prepopulated_fields = {'slug':('name',)}

# admin.site.register(Rating)
# admin.site.register(SubCategory)



from django.contrib import admin
from .models import Category, Brand, Product, Rating

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    fields = ('rating', 'value', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'brand', 'color', 'rating', 'stock', 'aviable')
    list_filter = ('category', 'brand', 'color')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [RatingInline]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'value', 'name')
    list_filter = ('product', 'rating')

