from django.contrib import admin
from django.urls import path, include

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]

