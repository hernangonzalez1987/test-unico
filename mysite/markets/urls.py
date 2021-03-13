from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateMarketsView.as_view(),name="Market List/Create"), 
    path('<int:pk>', views.RetrieveUpdateDestroyMarketView.as_view(), name='Market Update/Delete'),
]