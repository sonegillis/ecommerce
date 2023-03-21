from django.shortcuts import render
from rest_framework import generics


from inventory.models import Category, Product
from inventory.serializers import CategorySerializer, ProductSerializer


def index(request):
    return render(request, "inventory/index.html")


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(parent_category=None)


class CategoryProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs.get('slug'))
        return Product.objects.filter(category=category)


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
