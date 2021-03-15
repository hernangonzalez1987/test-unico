from django.http import JsonResponse
from rest_framework.views import exception_handler

def response_error_handler(request, exception=None):
    response = exception_handler(exception, None)
       
    return JsonResponse({'message':response.status_text}, status=response.status_code)
