from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from alocaVaga import serializers


from .models import Alocada, Vazia
from alocaVaga.serializers import AlocadaSerializer, VaziaSerializer


class AlocadaViewSet(viewsets.ModelViewSet):
    queryset = Alocada.objects.all()
    serializer_class = AlocadaSerializer


class VaziaViewSet(viewsets.ModelViewSet):
    queryset = Vazia.objects.all()
    serializer_class = VaziaSerializer
