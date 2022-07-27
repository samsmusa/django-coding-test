from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.viewsets import ModelViewSet


from django.db.models import Prefetch
from product.models import Product, ProductVariant, ProductVariantPrice

from product.serializer import ProductSerialize, ProductVariantSerializer


@api_view(['GET'])
def product_api(request):
    queryset = Product.objects.all()
    query_stirng = {}
    for key in request.query_params:
        query_stirng[key] = request.query_params[key]
    print(query_stirng)

    queryset = queryset.prefetch_related(Prefetch('pvariantprice', queryset=ProductVariantPrice.objects.filter(price__lt=1000)))\
        .filter(**{"pvariantprice__price__lt":1000}).distinct()
    serialize = ProductSerialize(queryset, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Product_variant_api(request):
    queryset = ProductVariant.objects.all()
    serializer = ProductVariantSerializer(many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @APIView()
class ProductAPI(ModelViewSet):
    # http_method_names = ['get']
    # queryset = Product.objects.all()
    serializer_class = ProductSerialize

    def get_queryset(self):
        queryset = Product.objects.all()
        filter_string =  {}
        for key in dict(self.request.query_params):
            print( key)
            filter_string[key] = self.request.query_params[key]
        print(filter_string)
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     print(kwargs)
        # return context
    