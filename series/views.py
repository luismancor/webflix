from .serializers import DatosSerializer, AccionesSerializer
from rest_framework import generics,permissions

from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Datos, MoverRobot

class DataSensor(APIView):
    #permission_classes = [permissions.IsAuthenticated,]
    #permission_classes = [TokenHasScope]
    #required_scopes = ['arduino','leer']
    def get(self, request):
        
        try:
            temperatura = request.GET['temperatura']
            humedad = request.GET['humedad']
            token = request.GET['token']
            if token == 'qwerty':

                datos = Datos.objects.get(id=2)
                datos.temperatura = temperatura
                datos.humedad = humedad
                datos.save()

                content = [{
                    "Mensaje": "Update Success" 
                }]
                return Response(content)
            else:
                content = [{
                    "Mensaje": "Acceso Denegado" 
                }]
                return Response(content)
        except:
            content = [{
                    "Mensaje": "Acceso Denegado" 
                }]
            return Response(content)

class AccionesRobot(APIView):  
    #permission_classes = [TokenHasScope,permissions.IsAuthenticated]
    permission_classes = [TokenHasScope]
    required_scopes = ['android']
    def get(self, request):
        
        accion = request.GET['accion']
  
        datos = MoverRobot.objects.get(id=2)
        datos.avanzar = accion
    
        datos.save()

        content = [{
            "Mensaje": "Update Success" 
        }]
        return Response(content)


class DatosList(generics.ListAPIView):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer

class AccionesList(generics.ListAPIView):
    queryset = MoverRobot.objects.all()
    serializer_class = AccionesSerializer

