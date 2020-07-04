from django.contrib import admin

from .models import User,FoodItem,SaleHistory

#Register your models here.
admin.site.register(User)
admin.site.register(FoodItem)
admin.site.register(SaleHistory)
