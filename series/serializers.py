from rest_framework import serializers
from .models import Datos, MoverRobot


class DatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datos
        fields = ['id', 'temperatura', 'humedad','updated']


class AccionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoverRobot
        fields = ['accion']

