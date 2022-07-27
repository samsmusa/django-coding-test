from rest_framework import serializers
from product.models import Product, ProductVariant, ProductVariantPrice


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['variant_title']


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    # product_variant_one = ProductVariantSerializer()
    # product_variant_three = ProductVariantSerializer()
    # product_variant_three = ProductVariantSerializer()
    variant = serializers.SerializerMethodField('fulltitle')

    def fulltitle(self, instance):
      try:
        size = instance.product_variant_three.variant_title
      except:
        size=''
      try:
        color = instance.product_variant_two.variant_title
      except:
        color=''
      try:
        style = instance.product_variant_one.variant_title
      except:
        style=''
      return f'{size}/{color}/{style}'

    class Meta:
        model = ProductVariantPrice
        fields = ['variant','stock', 'price']


class ProductSerialize(serializers.ModelSerializer):
    pvariantprice = ProductVariantPriceSerializer(many=True)
    # pvarinat = serializers.PrimaryKeyRelatedField(
    #   queryset = ProductVariant.objects.all(),
    #   many=True
    # )

    class Meta:
        model = Product
        fields = ['id', 'title', 'sku', 'pvariantprice']
        depth = 3
