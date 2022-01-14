from rest_framework import serializers
from ititems.models import Ititems


class ItitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ititems
        fields = "__all__"