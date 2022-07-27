from product.models import Product
from product.serializer import ProductSerializer


from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

from django.shortcuts import HttpResponse

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    print(serializer.data)
    return Response(serializer.data)
