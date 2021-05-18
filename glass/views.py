from django.db.models import query
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Company, Car, Model, Glass
from .serializers import CompanySerializer, CarSerializer, GlassSerializer, ModelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CompanyList(ReadOnlyModelViewSet):
    queryset = Company.objects.order_by("name")
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CarList(ReadOnlyModelViewSet):
    queryset = Car.objects.order_by("name")
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']


class ModelList(ReadOnlyModelViewSet):
    queryset = Model.objects.order_by("name")
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car']


class GlassList(ReadOnlyModelViewSet):
    serializer_class = GlassSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['car', 'model']

    def get_queryset(self):
        queryset = Glass.objects.order_by("name")
        carname = self.request.GET.get('search')
        if carname is not None:
            queryset = Glass.objects.filter(car__name__icontains=carname.lower())
        return queryset
