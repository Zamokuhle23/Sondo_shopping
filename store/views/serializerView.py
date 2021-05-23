from rest_framework import viewsets
from customers.models import Customer
from store.models import Category, Product, Order
from store.models.Comment import Comment
from store.serializers import CommentSerializer, CategorySerializer, OrderSerializer, ProductSerializer, \
    CustomerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        return Customer.objects.all()