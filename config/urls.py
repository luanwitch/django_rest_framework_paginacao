from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from product import views
from django.http import HttpResponse

def home(request):
    return HttpResponse("API funcionando! 🚀")

urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
