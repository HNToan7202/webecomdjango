from rest_framework import serializers
from store.models import Cart,Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart 
        fields=('name',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=('name',)