from django.shortcuts import render

from rest_framework import generics

from inventory.models import Category, Product
from inventory.serializers import CategorySerializer, ProductSerializer


# Create your views here.

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
