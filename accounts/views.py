from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from utils.custom_exception import CustomExceptionHandler


# Create your views here.

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def status_521(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'POST'})
    elif request.method == 'GET':
        raise ValidationError(521, 'You are not allowed to do this')

    return None



@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def status_522(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'POST'})
    elif request.method == 'GET':
        raise CustomExceptionHandler(522, 'You are not allowed to do this', "Hello")

    return None