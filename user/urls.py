from django.contrib import admin
from django.urls import path, include
from user import views

from user.views import JwtTokenObtainPairView
from user.views import OnlyAuthenticatedUserView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # user/
    path('', views.UserView.as_view()),
    # path('user/', views.UserAPIView.as_view()),
    path('api/token/', views.JwtTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/Jwt/token/', JwtTokenObtainPairView.as_view(), name='jwt_token'),
    #     path('api/authonly/', OnlyAuthenticatedUserView.as_view()),
]
