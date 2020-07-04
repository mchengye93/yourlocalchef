from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from foods.serializers import UserSerializer,FoodItemSerializer
from foods.models import User,FoodItem,SaleHistory

class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields=('name','location',)
    search_fields = ('name',)

class FoodItemList(ListAPIView):
    queryset=FoodItem.objects.all()
    serializer_class= FoodItemSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields=('price',)
    search_fields=('name', 'description')

