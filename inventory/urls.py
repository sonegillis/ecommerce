from django.urls import path

from inventory.views import CategoryView, ProductView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:slug>', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
]
