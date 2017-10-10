from django.shortcuts import render
import rest_framework_filters as filters
from rest_framework import serializers, viewsets
from .models import Canvas, CanvasItem


class CanvasItemFilter(filters.FilterSet):
    class Meta:
        model = CanvasItem
        fields = {'canvas': ['exact']}

class CanvasItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasItem
        fields = ('color', 'title', 'description', 'order')

class CanvasSerializer(serializers.ModelSerializer):
    items = CanvasItemSerializer(many=True, read_only=True)

    class Meta:
        model = Canvas
        fields = ('title', 'creation_date', 'items')

class CanvasViewSet(viewsets.ModelViewSet):
    queryset = Canvas.objects.all()
    serializer_class = CanvasSerializer

class CanvasItemsViewSet(viewsets.ModelViewSet):
    filter_class = CanvasItemFilter
    queryset = CanvasItem.objects.all()
    serializer_class = CanvasItemSerializer

