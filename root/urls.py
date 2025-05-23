from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from root.views import api_exception_handler, CrashTestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/bad/', api_exception_handler, name='api_exception_handler'),
    path('api/crash/', CrashTestView.as_view()),

    path('api/users/', include('accounts.urls')),
]


handler404 = 'root.views.custom_404_view'
handler500 = 'root.views.custom_500_view'
