from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView, ProductListView, testReact
from product.views.variant import VariantView, VariantCreateView, VariantEditView


from .views import productAPI 

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
    path('test/', testReact, name='test.product'),




    path('plist', productAPI.product_list, name='plistapi'),
    path('plist/<pk>', productAPI.product_details, name='pdetailstapi'),
    path('pvlist/', productAPI.product_variant_list, name='pvlist'),
    path('pvplist/', productAPI.product_variant_price_list, name='pvplist'),
    path('vlist/', productAPI.variant_list, name='vlist'),
]

