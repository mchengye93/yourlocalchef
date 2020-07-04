from rest_framework.generics import ListAPIView

from foods.serializers import UserSerializer,FoodItemSerializer
from foods.models import User,FoodItem,SaleHistory

class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class FoodItemList(ListAPIView):
    queryset=FoodItem.objects.all()
    serializer_class= FoodItemSerializer

