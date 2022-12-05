from rest_framework import serializers
from alocaVaga.models import Alocada, Vazia


class AlocadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alocada
        fields = "__all__"


class VaziaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vazia
        fields = "__all__"
