from django.http import JsonResponse
from rest_framework.response import Response


def standard_response(success: bool, data, error_msg)-> Response:
    if success:
        return Response({'success': True, 'message': data})
    elif data:
        return Response({'success': False, 'error': error_msg, 'message': data})
    else:
        return Response({'success': False, 'error': error_msg})


def standard_json_response(success: bool, data, error_msg, status_code: int)-> JsonResponse :
    if success:
        return JsonResponse({'success': True, 'message': data}, status=status_code)
    elif data:
        return JsonResponse({'success': False, 'error': error_msg, 'message': data}, status=status_code)
    else:
        return JsonResponse({'success': False, 'error': error_msg}, status=status_code)