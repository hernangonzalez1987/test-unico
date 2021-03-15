from django.urls import include, path
import markets.utils
from django.http import HttpResponse
from rest_framework.views import exception_handler
import json

def response_error_handler(request, exception=None):
    response = exception_handler(exception, None)

    response_data = {}
    response_data['message'] = response.status_text
        
    return HttpResponse(json.dumps(response_data), status=response.status_code)


handler500 = response_error_handler
handler404 = response_error_handler

urlpatterns = [
    path('markets/', include('markets.urls')),
]


