from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .pagination import ItemPagination
from .models import Item

# Create your views here.


class ItemList(ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ItemPagination

    def get_queryset(self):
        queryset = Item.objects.order_by("name")
        carname = self.request.GET.get('car')
        if carname is not None:
            queryset = Item.objects.filter(
                car__icontains=carname.lower())
        itemname = self.request.GET.get('item')
        if itemname is not None:
            queryset = Item.objects.filter(
                name__icontains=itemname.lower())
        return queryset
