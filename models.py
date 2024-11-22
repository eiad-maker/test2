from django.db import models

# Create your models here.

class Product(models.Model) :
    name= models.CharField(max_length=50)
    price= models.DecimalField(max_digits=6, decimal_places=0)  
    content= models.TextField()
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    
    

class Add(models.Model):
    pass