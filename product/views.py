from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from product.models import Product
from product.serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')  
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
