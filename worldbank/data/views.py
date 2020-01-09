from data.models import Country, Indicator, Stat
from data.serializers import CountrySerializer, IndicatorSerializer, StatSerializer
from rest_framework import generics, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class IndicatorList(generics.ListAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class StatView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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


class StatFilterView(APIView):
    def get(self, request):
        country_list = request.data['countrys']
        stats = Stat.objects.filter(country__in=country_list)
        serializer = StatSerializer(stats, many=True)

        return Response(serializer.data)
