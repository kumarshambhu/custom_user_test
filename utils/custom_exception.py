from rest_framework import status
from rest_framework.exceptions import APIException


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