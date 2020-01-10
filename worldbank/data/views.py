from data.models import Country, Indicator, Stat
from data.serializers import CountrySerializer, IndicatorSerializer, StatSerializer
from rest_framework import generics, status, mixins, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from data.settings import INDICATORS_LIST


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


class IndicatorList(generics.ListAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class StatView(generics.ListAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = Stat.objects.all()
        query_params = self.request.query_params
        if countries := query_params.get('countries', None):
            countries = countries.split(',')
            queryset = queryset.filter(country__in=countries)
        if years := query_params.get('years', None):
            years = years.split(',')
            queryset = queryset.filter(year__in=years)
        return queryset


    def get_object(self, pk):
        return Stat.objects.get(pk=pk)

    def patch(self, request):
        pk = request.data['id']
        stat_object = self.get_object(pk)
        serializer = StatSerializer(stat_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(code=400, data="wrong parameters")
