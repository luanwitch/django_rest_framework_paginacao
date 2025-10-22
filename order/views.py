# order/views.py

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer  
from .pagination import CustomOrderPagination

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomOrderPagination  

    def get_queryset(self):
        """
        This view returns a list of orders filtered for the
        currently authenticated user.
        """
        user = self.request.user
        
        return self.queryset.filter(user=user)