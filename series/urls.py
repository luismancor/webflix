from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from series import views


urlpatterns = [
   
    path('datos/', views.DatosList.as_view(), name='datos'),
    path('acciones/', views.AccionesList.as_view(), name='acciones'),
    
    path('send-data/', views.DataSensor.as_view(), name='data'),
    path('send-accion/', views.AccionesRobot.as_view(), name='accion'),
     
]

urlpatterns = format_suffix_patterns(urlpatterns)
