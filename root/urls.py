from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView


def error_404(request, exception):
    return JsonResponse({"error": "API Not Found"}, status=404)

def error_500(request,):
    return JsonResponse({"error": "Server error"}, status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/users/', include('accounts.urls')),
]

handler404 = error_404
handler500 = error_500