from rest_framework import serializers

from .models import MyInventory


class DeleteSerializer(serializers.Serializer):
    hard_delete = serializers.BooleanField(required=True)


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInventory
        fields = ('id',
                  'name',
                  'is_deleted'
                  )
