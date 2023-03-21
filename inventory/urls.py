from django.urls import path

from inventory.views import CategoryView, ProductView, CategoryProductsView, index

urlpatterns = [
    path('', index),
    path('categories/', CategoryView.as_view()),
    path('category/<str:slug>/products/', CategoryProductsView.as_view()),
    path('products/', ProductView.as_view()),
]
