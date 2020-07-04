from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from foods.serializers import UserSerializer,FoodItemSerializer
from foods.models import User,FoodItem,SaleHistory

class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=('name','location',)

class FoodItemList(ListAPIView):
    queryset=FoodItem.objects.all()
    serializer_class= FoodItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields=('price',)

