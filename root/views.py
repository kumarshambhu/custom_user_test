from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView



def custom_404_view(request, exception:Exception) -> JsonResponse:
    print('custom 404 view', exception)
    return JsonResponse({
        'status_code': 404,
    })


def custom_500_view(request):
    return render(request, "errors/500.html", status=500)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def api_exception_handler(request,):
    print('api_exception_handler', request)
    #raise UserBannedException("This user is banned.")

@permission_classes([AllowAny])
class CrashTestView(APIView):
    def get(self, request):
        raise ValueError("This is a test exception")
