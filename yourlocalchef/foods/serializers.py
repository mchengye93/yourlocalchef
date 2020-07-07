from rest_framework import serializers
from foods.models import User,FoodItem,SaleHistory

class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = ('user','id','name','description','image', 'price','quantity','sale_start','sale_end')

class UserSerializer(serializers.ModelSerializer):
    
    foodItems = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id','name','email','location','image','description','joined','foodItems')
        read_only_fields = ('joined',)


    #Adding extra fields to API
    # def to_representation(self,instance):
    #         data=super().to_representation(instance)
    #         data['is_on_sale']= instance.is_on_sale()
    #         return data

    
