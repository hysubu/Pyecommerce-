from django.db import models

# Create your models here.
class ProductCatagory(models.Model):
    catagory_name = models.CharField(max_length=300)
    other = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.catagory_name

class SubCatagory(models.Model):
    catagory_name = models.ForeignKey(ProductCatagory, on_delete=models.CASCADE)
    subcatagorie_name = models.CharField(max_length=200)


    def __str__(self):
        return self.subcatagorie_name





class Product(models.Model):
    subcatagory = models.ForeignKey(SubCatagory, on_delete=models.CASCADE)
    productName =  models.CharField( max_length=200)
    title =  models.CharField(max_length=100)
    actual_price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.TextField()
    about = models.JSONField(null=True, blank=True)
    image1 = models.FileField(null=True , blank=True , upload_to="productimages")
    image2 = models.FileField(null=True , blank=True , upload_to="productimages")
    image3 = models.FileField(null=True , blank=True , upload_to="productimages")
    image4 = models.FileField(null=True , blank=True , upload_to="productimages")

class ProduImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField( upload_to='productimages')


class PaymentMethod(models.Model):
    methods_name = models.CharField(max_length=100)

