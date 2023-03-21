from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from inventory.models import Category, Product, ProductFeature, ProductVariation


class CategorySerializer(ModelSerializer):
    product_count = serializers.SerializerMethodField()
    child_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    @staticmethod
    def _recurse_count_products_in_category(category, product_count=0):
        if category.categories and category.categories.all().count():
            for _category in category.categories.all():
                product_count += CategorySerializer._recurse_count_products_in_category(_category, product_count)
        product_count += category.products.all().count() if category.products else 0
        return product_count

    def get_product_count(self, category):
        return CategorySerializer._recurse_count_products_in_category(category, 0)

    def get_child_categories(self, category):
        return CategorySerializer(category.categories.all(), many=True).data


class ProductVariationSerializer(ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = "__all__"


class ProductFeatureSerializer(ModelSerializer):
    product_variation = ProductVariationSerializer(read_only=True)

    class Meta:
        model = ProductFeature
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    product_feature = ProductFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
