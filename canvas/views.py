from django.shortcuts import render
from .models import Canvas, CanvasItem
from rest_framework import serializers, viewsets


class CanvasItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasItem
        fields = {'color', 'title', 'description', 'order'}

class CanvasSerializer(serializers.ModelSerializer):
    items = CanvasItemSerializer(many=True, read_only=True)

    class Meta:
        model = Canvas
        fields = {'title', 'creation_date'}

class CanvasViewSet(viewsets.ModelViewSet):
    queryset = Canvas.objects.all()
    serializer_class = CanvasSerializer

