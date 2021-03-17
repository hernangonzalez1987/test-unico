from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import MarketSerializer, MarketUpdatedSerializer
from .models import Market
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.http import JsonResponse


class MultipleFieldsSearch:
    def get_queryset(self):
        queryset = Market.objects.all()

        for field in self.lookup_fields:
            if self.request.query_params.get(field):

                value = self.request.query_params.get(field)
                filter = field + '__exact'
                queryset = queryset.filter(
                    **{filter: self.request.query_params.get(field)})

        return queryset


class ListCreateMarketsView(MultipleFieldsSearch, ListCreateAPIView):

    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    lookup_fields = ['district', 'region_5', 'name', 'address_city']

    @extend_schema(description='Create a Market')
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @extend_schema(
        description='List Markets with optional filters',
        parameters=[
            OpenApiParameter(name='district', description='District',
                             required=False, type=str, location='query'),
            OpenApiParameter(name='region_5', description='Region',
                             required=False, type=str, location='query'),
            OpenApiParameter(name='name', description='Name',
                             required=False, type=str, location='query'),
            OpenApiParameter(name='address_city', description='City',
                             required=False, type=str, location='query'),
        ],
    )
    def get(self, request, *args, **kwargs):

        if not bool(set(self.request.query_params).intersection(self.lookup_fields)):
            return JsonResponse({'message': "Should include at least one query param: [district,region_5,name,address_city]"}, status=400)

        return self.list(request, *args, **kwargs)


class RetrieveUpdateDestroyMarketView(RetrieveUpdateDestroyAPIView):

    queryset = Market.objects.all()
    lookup_field = 'registration_code'
    serializer_class = MarketUpdatedSerializer

    @extend_schema(description='Gets a Market by Registration Code')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(description='Deletes a Market by Registration Code')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(description='Partially updates a Market by Registration Code')
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(description='Updates a Market by Registration Code')
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
