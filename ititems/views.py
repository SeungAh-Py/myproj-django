from rest_framework import viewsets
from ititems.models import Ititems
from ititems.serializers import ItitemsSerializer


class ItitemsViewSet(viewsets.ModelViewSet):
    queryset = Ititems.objects.all()
    serializer_class = ItitemsSerializer