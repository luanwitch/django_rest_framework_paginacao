from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, AccountSerializer
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dados_protegidos_view(request):
    conteudo = {'message': f'Olá, {request.user.username}.'}
    return Response(conteudo)
