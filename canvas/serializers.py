from rest_framework import serializers
from .models import Canvas, CanvasItem


class CanvasItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasItem
        fields = ('color', 'title', 'description', 'order')

class CanvasSerializer(serializers.ModelSerializer):
    items = CanvasItemSerializer(many=True, read_only=True)

    class Meta:
        model = Canvas
        fields = ('title', 'creation_date', 'items')
