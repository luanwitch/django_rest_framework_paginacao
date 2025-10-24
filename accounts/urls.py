from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, dados_protegidos_view

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('dados-protegidos/', dados_protegidos_view, name='dados_protegidos'),
]


