from http.client import responses

from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

class CustomExceptionHandler(APIException):
    status_code = status.HTTP_102_PROCESSING
    default_detail = 'Invalid input.'
    default_code = 'invalid'
    response = 'testing'



def custom_exception_handler(exc, context):
    print('custom_exception_handler')
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_generic_error,
        'CustomExceptionHandler': _handle_generic_error,
    }

    response = exception_handler(exc, context)
    print(f'response: {response}')
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        print(f'exception_class : {exception_class}')
        return handlers[exception_class](exc, context, response)
    return response

def _handle_generic_error(exc, context, response):
    print(f'_handle_generic_error: {response}')
    return response