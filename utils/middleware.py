from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Log the exception
        logger.error(f"Unhandled exception: {str(exception)}", exc_info=True)

        # Return a custom response
        return JsonResponse({
            'error': 'An unexpected error occurred',
            'details': str(exception)
        }, status=500)