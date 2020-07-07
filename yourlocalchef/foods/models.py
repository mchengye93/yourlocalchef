from django.db import models
from datetime import datetime

class User(models.Model):
        cities =  (
        ('BK', 'Berkeley'),
        ('OAK', 'Oakland'),
        ('NY', 'New York'),
        ('SF', 'San Francisco'),
        ('SJ', 'San Jose'),
        ('LA', 'Los Angeles'),
        )
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        location = models.CharField(max_length=50,choices=cities)
        description = models.TextField(blank=True)
        joined= models.DateTimeField(default=datetime.now, blank=True)
        image= models.ImageField(upload_to = 'images/' ,blank=True)
        

class FoodItem(models.Model):
        user = models.ForeignKey(User,related_name='foodItems', on_delete = models.CASCADE)
        name= models.CharField(max_length=50)
        description = models.TextField(blank=True)
        image= models.ImageField(upload_to = 'images/',blank=True)
        price = models.DecimalField(max_digits=5, decimal_places=2)
        quantity = models.IntegerField(default=0)
        sale_start=models.DateTimeField(default=datetime.now)
        sale_end=models.DateTimeField(default=datetime.now)

class SaleHistory(models.Model):
        food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=5, decimal_places=2)
        quantity = models.IntegerField()
        date= models.DateTimeField(default=datetime.now, blank=True)


       
        
        