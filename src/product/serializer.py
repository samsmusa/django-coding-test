from rest_framework import serializers


class ProductVariantPriceSerializer(serializers.Serializer):
  price = serializers.FloatField()
  stock = serializers.FloatField()

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    sku = serializers.CharField()
    description = serializers.CharField()
    
