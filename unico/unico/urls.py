from django.urls import include, path
from .views import response_error_handler

handler500 = response_error_handler
handler404 = response_error_handler

urlpatterns = [
    path('markets/', include('markets.urls')),
]