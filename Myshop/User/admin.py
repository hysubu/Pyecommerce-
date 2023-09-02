from django.contrib import admin
from . models import *
# Register your models here.



@admin.register(Useraccount)
class Usermodel(admin.ModelAdmin):
    list_display = ["id" ]

@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ["id" ]

@admin.register(AddtoCart)
class Addtocart(admin.ModelAdmin):
    list_display = ["id" ]



@admin.register(OrderDetail)
class OrderDetail(admin.ModelAdmin):
    list_display = ["id" ]


