from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MarketSerializer,MarketUpdatedSerializer
from .models import Market

# Create your views here.
class ListCreateMarketsView(ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class RetrieveUpdateDestroyMarketView(RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketUpdatedSerializer
