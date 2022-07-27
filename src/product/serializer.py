from rest_framework import serializers

from product.models import ProductVariantPrice

class VarintSerializer(serializers.Serializer):
  title = serializers.CharField()
  description = serializers.CharField()
  active = serializers.BooleanField()


class ProductVariantSerializer(serializers.Serializer):
  variant_title = serializers.CharField()
  variant = VarintSerializer()


class ProductVariantPriceSerializer(serializers.Serializer):
  price = serializers.FloatField()
  stock = serializers.FloatField()
  product_variant_one = ProductVariantSerializer()
  product_variant_two = ProductVariantSerializer()
  product_variant_three = ProductVariantSerializer()

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    sku = serializers.CharField()
    description = serializers.CharField()
    pvariantprice = ProductVariantPriceSerializer(many=True)

