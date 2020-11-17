from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=100,default="")
    desc=models.CharField(max_length=10000,default="")
    publish_date=models.DateField()
    price=models.CharField(max_length=20,default="")
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    desc_help=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=500)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    phone=models.CharField(max_length=15,default="")


    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True) 
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7] + "..."

