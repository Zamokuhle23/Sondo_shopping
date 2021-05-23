from rest_framework import serializers

from customers.models import Customer
from store.models import Category, Order, Product
from store.models.Comment import Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields  = ["id","author","date_posted","product_connected","content"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields  = ["id","product","customer","quantity","price","date","address","phone","completed"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields  = ["id","name","price","category","description","image","date"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields  = ["id","customer","image","email","phone"]