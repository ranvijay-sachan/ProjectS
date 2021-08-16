from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import MyInventory
from .serializers import InventorySerializer, DeleteSerializer
from .permissions import MyCustomPermissions


class InventoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving inventory.
    """
    queryset = MyInventory.objects.all()
    serializer_class = InventorySerializer
    # permission_classes = (MyCustomPermissions,)
    http_method_names = ['get', 'post', 'put', 'patch']

    @action(detail=True, methods=['put'], serializer_class=DeleteSerializer)
    def custom_delete(self, request, pk=None):
        queryset = MyInventory.objects.all()
        inventory = get_object_or_404(queryset, pk=pk)
        obj = MyInventory.objects.get(id=inventory.id)
        serializer = DeleteSerializer(data=request.data)
        if serializer.is_valid():
            hard_delete = serializer.data['hard_delete']
            if hard_delete:
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            obj.soft_delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






