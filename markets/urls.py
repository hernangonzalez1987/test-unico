from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateMarketsView.as_view(),name="Market List/Create"), 
    path('<str:registration_code>', views.RetrieveUpdateDestroyMarketView.as_view(), name='Market Update/Delete'),
]