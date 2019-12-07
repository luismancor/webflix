from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from series import views

from rest_framework.authtoken.views import obtain_auth_token
from series import views
from .views import tokenValidator, DatosList

urlpatterns = [
    path('series/', views.SerieList.as_view()),
    path('datos/', views.DatosList.as_view()),
    path('series/<int:pk>/', views.SerieDetail.as_view()),


    #Token
    path('token/', views.TokenResponse.as_view(), name='token'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('tokenValidator/', views.tokenValidator)
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
