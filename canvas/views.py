from django.shortcuts import render
import rest_framework_filters as filters
from rest_framework import viewsets
from .models import Canvas, CanvasItem
from .serializers import CanvasItemSerializer, CanvasSerializer


class CanvasItemFilter(filters.FilterSet):
    class Meta:
        model = CanvasItem
        fields = {'canvas': ['exact']}

class CanvasViewSet(viewsets.ModelViewSet):
    queryset = Canvas.objects.all()
    serializer_class = CanvasSerializer

class CanvasItemsViewSet(viewsets.ModelViewSet):
    filter_class = CanvasItemFilter
    queryset = CanvasItem.objects.all()
    serializer_class = CanvasItemSerializer

