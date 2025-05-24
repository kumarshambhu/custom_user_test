from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


@permission_classes([AllowAny])
class CrashTestView(APIView):
    def get(self, request):
        raise ValueError("This is a test exception")