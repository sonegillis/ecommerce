from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from inventory.models import Category, Product, ProductFeature, ProductVariation


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


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
