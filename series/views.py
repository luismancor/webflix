from .models import Serie
from .serializers import SerieSerializer, DatosSerializer
from rest_framework import generics

#testing

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes

from .models import Datos

class TokenResponse(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        
        temperatura = request.GET['temperatura']
        humedad = request.GET['humedad']

        datos = Datos.objects.get(id=1)
        datos.temperatura = temperatura
        datos.humedad = humedad
        datos.save()


        content = [{
            "Mensaje": "Update Success" 
        }]
        return Response(content)

    def post(self, request):
        
        temperatura = request.POST['temperatura']
        humedad = request.POST['humedad']
        content = {
            "temperatura": temperatura,
            "humedad": humedad,
        }
        return Response(content)


@api_view(["POST"])
def tokenValidator(request):
    token = request.data.get("token")
    try:
        tokenValidator = Token.objects.get(key=token)
    except:
        return Response({"vale":"me salio un error"},status = 202)
    if tokenValidator:
        return Response(
            {'Message': {
                        "codigo": '',
                        "mensaje" : ''
                    },
                    "token":tokenValidator.key,
                    "codigoError":''
                  }
        )   
    else:
        return Response(
            {'Message': {
                        "codigo": '',
                        "mensaje" : ''
                    },
                    "token":'',
                    "codigoError":''
                  }
        )
 


class DatosList(generics.ListCreateAPIView):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer



class SerieList(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class SerieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
