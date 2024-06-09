from datetime import datetime

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Город, Улица, Магазин
from .serializers import ГородSerializer, УлицаSerializer, МагазинSerializer


class ГородViewSet(viewsets.ModelViewSet):
    queryset = Город.objects.all()
    serializer_class = ГородSerializer


class УлицаViewSet(viewsets.ModelViewSet):
    queryset = Улица.objects.all()
    serializer_class = УлицаSerializer


class МагазинViewSet(viewsets.ModelViewSet):
    queryset = Магазин.objects.all()
    serializer_class = МагазинSerializer


@api_view(['GET'])
def магазины(request):
    street = request.GET.get('street')
    city = request.GET.get('city')
    open = request.GET.get('open')

    queryset = Магазин.objects.all()

    if street:
        queryset = queryset.filter(улица__название=street)

    if city:
        queryset = queryset.filter(город__название=city)

    if open is not None:
        if open == '1':
            queryset = queryset.filter(время_открытия__lte=datetime.now(), время_закрытия__gte=datetime.now())
        else:
            queryset = queryset.exclude(время_открытия__lte=datetime.now(), время_закрытия__gte=datetime.now())

    serializer = МагазинSerializer(queryset, many=True)

    return Response(serializer.data)