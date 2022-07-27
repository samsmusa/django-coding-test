from product.models import Product, ProductVariant, ProductVariantPrice, Variant
from product.serializer import ProductSerializer, VarintSerializer, ProductVariantPriceSerializer, ProductVariantSerializer


from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from django.shortcuts import HttpResponse, get_object_or_404

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view()
def variant_list(request):
    queryset = Variant.objects.all()
    serializer = VarintSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_variant_list(request):
    queryset = ProductVariant.objects.all()
    serializer = ProductVariantSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_variant_price_list(request):
    queryset = ProductVariantPrice.objects.all()
    serializer = ProductVariantPriceSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_details(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def variant_detials(request, pk):
    variant = get_object_or_404(Variant, id=pk)
    serializer = VarintSerializer(variant)
    return Response(serializer.data)

@api_view()
def product_variant_detials(request, pk):
    product_varinat = get_object_or_404(ProductVariant, id=pk)
    serialzier = ProductVariantSerializer(product_varinat)
    return Response(serialzier.data)


@api_view()
def product_variant_price_detials(request, pk):
    product_variant_price = get_object_or_404(ProductVariantPrice, id=pk)
    serializer = ProductVariantPriceSerializer(product_variant_price)
    return Response(serializer.data)
