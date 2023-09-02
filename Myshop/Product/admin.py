from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(ProductCatagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(SubCatagory)
class Subcatagory(admin.ModelAdmin):
    list_display = ["id" , "subcatagorie_name"]




@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ["id","productName"]
