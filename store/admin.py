from django.contrib import admin
from .models import Product
from .models import Category,Customer
# Register your models here.


class AdminProduct(admin.ModelAdmin):                #to show name of products
    list_display=['name','price' ,'category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)

