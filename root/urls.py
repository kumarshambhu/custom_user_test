from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from root.views import CrashTestView
from utils.common_utils import standard_json_response


def error_404(request, exception):
    return standard_json_response(False, "Unable to Find API", "API Not Found", 404)


def error_500(request, ):
    return standard_json_response(False, "Error in processing on server", "Server error", 500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/users/', include('accounts.urls')),

    path('api/crash/', CrashTestView.as_view()),
]

handler404 = error_404
handler500 = error_500
