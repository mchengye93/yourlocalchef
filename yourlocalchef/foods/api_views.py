from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from foods.serializers import UserSerializer,FoodItemSerializer
from foods.models import User,FoodItem,SaleHistory

class DefaultPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit=100



class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields=('name','location',)
    search_fields = ('name',)
    pagination_class = DefaultPagination

class FoodItemList(ListAPIView):
    queryset=FoodItem.objects.all()
    serializer_class= FoodItemSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields=('price',)
    search_fields=('name', 'description')
    pagination_class = DefaultPagination

