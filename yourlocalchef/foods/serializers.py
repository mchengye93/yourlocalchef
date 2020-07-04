from rest_framework import serializers
from foods.models import User,FoodItem,SaleHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','location','description','joined')

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id','name','description','price','quantity','sale_start','sale_end')
    
    #Adding extra fields to API
    # def to_representation(self,instance):
    #         data=super().to_representation(instance)
    #         data['is_on_sale']= instance.is_on_sale()
    #         return data

    
