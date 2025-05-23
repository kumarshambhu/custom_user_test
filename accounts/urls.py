from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from accounts.models import CustomUser
from accounts.views import status_521


class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'age']


@api_view(['GET'])
def user_details(request):
    user = request.user
    client = get_object_or_404(CustomUser, id=user.token['user_id'])
    serializer = CustomUserModelSerializer(client, many=False)
    return Response(serializer.data)


urlpatterns = [
    path('details/', user_details),
    path('status/', status_521),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
