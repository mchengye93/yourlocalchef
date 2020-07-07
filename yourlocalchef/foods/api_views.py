from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from foods.serializers import UserSerializer,FoodItemSerializer
from foods.models import User,FoodItem,SaleHistory

class DefaultPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit=100



class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields=('name','location',)
    search_fields = ('name',)
    pagination_class = DefaultPagination

class UserCreate(CreateAPIView):
    serializer_class = UserSerializer

class FoodItemList(ListAPIView):
    queryset=FoodItem.objects.all()
    serializer_class= FoodItemSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields=('price',)
    search_fields=('name', 'description')
    pagination_class = DefaultPagination

class FoodItemCreate(CreateAPIView):
    serializer_class = FoodItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})
        except ValueError:
            raise ValidationError ({'price': 'A valid number is required'})
        return super().create(request, *args, **kwargs)
    

class FoodItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= FoodItem.objects.all()
    lookup_field= 'id'
    serializer_class= FoodItemSerializer

    #This is to remove cache if delete is success
    def delete(self,request, *args, **kwargs):
        fooditem_id = request.data.get('id')
        response = super().delete(request,*args, **kwargs)

        if response.status_code == 204:
            from django.core.cache import cache
            print('calling delete'+ cache.keys('*'))
        return response
    
    #This is to update cache if update is success
    def update(self,request,*args, **kwargs):
        response=super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            fooditem = response.data
            
        return response



