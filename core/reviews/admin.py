from django.contrib import admin
from reviews.models import Product, Brand, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_filter = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)    