from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductListView, testReact
from product.views.variant import VariantView, VariantCreateView, VariantEditView


from .views.productAPI import product_api, Product_variant_api, ProductAPI

from rest_framework.routers import DefaultRouter


app_name = "product"



urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(), name='list.product'),
    path('test/', testReact, name='test.product')
]

