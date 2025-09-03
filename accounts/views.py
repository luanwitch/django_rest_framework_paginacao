# accounts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dados_protegidos_view(request):

    conteudo = {'message': f'Olá, {request.user.username}! Se você está vendo isso, seu token funciona.'}
    return Response(conteudo)