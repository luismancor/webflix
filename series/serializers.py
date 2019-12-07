from rest_framework import serializers
from .models import Serie, Datos


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'name', 'release_date', 'rating', 'category']


class DatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datos
        fields = ['id', 'temperatura', 'humedad']
