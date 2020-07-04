from django.shortcuts import render
from .models import FoodItem
# Create your views here.
def homepage(request):
    food_items= FoodItem.objects
    return render(request, 'fooditems/home.html', {'fooditems':food_items})