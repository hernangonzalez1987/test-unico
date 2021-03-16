from django.urls import include, path
from .views import response_error_handler
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

handler500 = response_error_handler
handler404 = response_error_handler


urlpatterns = [
    path('markets/', include('markets.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
