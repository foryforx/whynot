from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Productdata(models.Model):
    skuid = models.CharField(max_length=200,primary_key = True)
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=5000)
    google_product_category = models.CharField(max_length = 100)
    product_type = models.CharField(max_length = 100)
    link = models.URLField(max_length = 2000)
    image_link = models.URLField(max_length = 2000)
    condition = models.CharField(max_length = 100)
    availability = models.CharField(max_length = 100)
    price = models.FloatField(default = 99999999.99)
    sale_price = models.FloatField(default = None, null=True, blank=True)
    brand = models.CharField(max_length = 100)
    gtin = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    size = models.CharField(max_length = 100)
    model_code = models.CharField(max_length = 100)
    created_date = models.DateTimeField('created_date',auto_now_add=True,blank=True)
    updated_date = models.DateTimeField('updated_date',auto_now=True,blank=True)
    
    def __str__(self):
        return self.skuid + "|" +  self.gtin + "|" + self.brand
        
    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)
        
class Wishlist(models.Model):
    productdata = models.ForeignKey(Productdata, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField('created_date',auto_now_add=True,blank=True)
    updated_date = models.DateTimeField('updated_date',auto_now=True,blank=True)
    
    def __str__(self):
        return self.productdata.skuid + "|" +  self.email + "|" 
        
class Productfeed(models.Model):
    product_feed_url = models.CharField(max_length=200,primary_key = True)
    client = models.CharField(max_length=200)
    created_date = models.DateTimeField('created_date',auto_now_add=True)
    updated_date = models.DateTimeField('updated_date',auto_now=True)
    
    def __str__(self):
        return self.Productfeed.product_feed_url + "|" +  self.client