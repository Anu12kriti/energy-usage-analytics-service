from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Site, EnergyReading
from .serializers import SiteSerializer, EnergyReadingSerializer


class SiteListCreateView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["utility"]

    search_fields = ["name", "address"]

    ordering_fields = ["name", "utility"]


class SiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class EnergyReadingListCreateView(generics.ListCreateAPIView):
    queryset = EnergyReading.objects.all()
    serializer_class = EnergyReadingSerializer


class EnergyReadingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnergyReading.objects.all()
    serializer_class = EnergyReadingSerializer