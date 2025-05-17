from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers
from accounts.models import CustomUser



class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','age']


@api_view(['GET'])
def user_details(request):
    user = request.user
    client = get_object_or_404(CustomUser, id=user.token['user_id'])
    serializer = CustomUserModelSerializer(client, many=False)
    return Response(serializer.data)
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/userdetails/', user_details),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
