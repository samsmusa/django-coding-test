from django.views import generic, View
from django.db.utils import IntegrityError
# from django.db.models.expressions import 
import json
from product.models import Product, ProductVariant, Variant, ProductVariantPrice, ProductImage
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Prefetch


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'
    # template_name = 'products/create.html'

    print('class')

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        context['component'] = 'root'

        return context

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)

        try:
            product = Product.objects.create(
                title=data['title'], description=data['desctiption'], sku=data['sku'])
        except:
            return HttpResponse(json.dumps({'message':'failed', 'status':403}),content_type="application/json")

        if len(data['image']) != 0:
            ProductImage.objects.create(
                product=product, file_path=data['image'])

        product_varinats = {}
        for obj in data['variant']:
            for tag in obj['tags']:
                try:
                    product_varinats[tag] = ProductVariant.objects.create(
                    variant_title=tag, variant=Variant.objects.get(pk=obj['option']), product=product)
                except:
                    return HttpResponse(json.dumps({'message':'some internal error', 'status':403}),content_type="application/json")

        product_varinats_price_variants = [
            'product_variant_one', 'product_variant_two', 'product_variant_three']

        result = list()
        for obj in data['product_variant_price']:
            list1 = dict()
            for index, tag in enumerate(obj['title'].split('/')):
                if tag in product_varinats:
                    list1[product_varinats_price_variants[index]
                          ] = product_varinats[tag]
            try:
                product_vprice = ProductVariantPrice.objects.create(
                    price=obj['price'], stock=obj['stock'], product=product, **list1)
                result.append(product_vprice)
            except:
                return HttpResponse(json.dumps({'message':'some internal error', 'status':403}),content_type="application/json")

        # return self.render_to_response({'message': 'success', "data": result})
        return HttpResponse(json.dumps({'message': 'success', 'status':200}),content_type="application/json")




class ProductListView(ListView):
    template_name = 'products/list.html'
    paginate_by = 3
    context_object_name = 'products'
    extra_context = {
        'product': True
    }

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        variants = Variant.objects.prefetch_related('productvariant_set').all()
        context['product'] = True
        context['variants'] = variants
        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        filter_string = {}
        filter_product_variant_price_string = {}

        for key in self.request.GET:
            if key in ['title__icontains', 'created_at__date']:
                if self.request.GET.get(key):
                    filter_string[key] = self.request.GET.get(key)

            if key in ['price__lte', 'price__gte']:
                pre = 'pvariantprice__'
                if self.request.GET.get(key):
                    filter_product_variant_price_string[key] = float(self.request.GET.get(key))
                    filter_string[pre+key] = float(self.request.GET.get(key))


            if key in ['variant_title__iexact']:
                print(key)
                if self.request.GET.get(key):
                    a = tuple(self.request.GET.get(key).split(' '))
                    print(a)
                    pre = 'pvariantprice__'
                    if a[0]=='Style':
                        query = 'product_variant_three__'+key
                        filter_string[pre+query] = a[1]
                        filter_product_variant_price_string[query] = a[1]
                    if a[0]=='Color':
                        query = 'product_variant_two__'+key
                        filter_string[pre+query] = a[1]
                        filter_product_variant_price_string[query] = a[1]
                    if a[0]=='Size':
                        query = 'product_variant_one__'+key
                        filter_string[pre+query] = a[1]
                        filter_product_variant_price_string[query] = a[1]
 
        return queryset.prefetch_related(Prefetch('pvariantprice', queryset=ProductVariantPrice.objects.filter(**filter_product_variant_price_string))).filter(**filter_string).distinct()


def testReact(request):
    return render(request, 'products/testreact.html', context={'component':'test'})
    

