from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from .models import Item
from .serializers import ItemSerializer


class ListRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class ItemViewSet(ListRetrieveViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'vendor_code',)
    filterset_fields = ('status',)
