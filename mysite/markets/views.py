from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MarketSerializer,MarketUpdatedSerializer
from .models import Market

class MultipleFieldsSearch:
    def get_queryset(self):
        queryset = Market.objects.all()

        for field in self.lookup_fields:
            if self.request.query_params.get(field): 

                value = self.request.query_params.get(field)
                filter = field + '__exact'
                queryset=queryset.filter(**{filter: self.request.query_params.get(field)})

        return queryset

# Create your views here.
class ListCreateMarketsView(MultipleFieldsSearch, ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    lookup_fields = ['district', 'region_5','name','city']

class RetrieveUpdateDestroyMarketView(RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    lookup_url_kwarg = 'registry'
    serializer_class = MarketUpdatedSerializer
