from django.db import models

# Create your models here.
    
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=150)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_descrip=models.CharField(max_length=300)
    product_date=models.DateField(auto_now=True)
    image=models.ImageField(upload_to="cart/images",default="")
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id=models.AutoField
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=17)
    descrip=models.CharField(max_length=600)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
    
