from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

class CustomExceptionHandler(APIException):
    status_code = status.HTTP_102_PROCESSING
    default_detail = 'Invalid input.'
    default_code = 'invalid'

    def __init__(self, status_code, default_detail, default_code):
        print('__init__')
        self.status_code = status_code
        self.default_detail = default_detail
        self.default_code = default_code
        super(CustomExceptionHandler, self).__init__()



def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_validation_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_generic_error,
        'CustomExceptionHandler': _handle_generic_error,
    }

    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response

def _handle_validation_error(exc, context, response):
    print(f'_handle_validation_error: {exc}')
    try:
        errors =  exc.detail
        error_message = errors.ErrorDetail
        print(f'_handle_validation_error: {error_message}')
    except Exception as e:
        print(f'_handle_error: {e}')
    return JsonResponse({'error': 'ddd1'}, status=400)
def _handle_generic_error(exc, context, response):
    return JsonResponse({'status_code': response.status_code, 'message': f'{exc}', 'default_code': f'{exc.get_codes()}'})