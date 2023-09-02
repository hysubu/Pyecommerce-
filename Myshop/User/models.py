from django.db import models
from Product.models import Product

# Create your models here.
class Useraccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    profile_image = models.TextField(null=True, blank=True)
    password_key = models.TextField()
    others = models.JSONField(null=True , blank=True)


class Address(models.Model):
    username = models.ForeignKey(Useraccount, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    contact = models.IntegerField()
    others = models.JSONField(null=True , blank=True)


class AddtoCart(models.Model):
    username = models.ForeignKey(Useraccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity =  models.IntegerField(null=True , blank=True)
    total_price = models.IntegerField()

class OrderDetail(models.Model):
    user = models.ForeignKey(Useraccount,on_delete=models.CASCADE, null= True , blank=True)
    order_id = models.TextField(null= True , blank=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    buynow_status = models.BooleanField(default=False , null= True , blank=True)
    total_price = models.IntegerField(null= True , blank=True)
    address = models.ForeignKey(Address , on_delete=models.CASCADE , null= True , blank=True)
    address_status = models.BooleanField(default=False,null=True,blank=True)
    payment_method = models.CharField(max_length=100 , null= True , blank=True) 
    payment_status = models.BooleanField(default=False , null=True , blank=True)


