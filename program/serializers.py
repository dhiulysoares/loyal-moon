from rest_framework import serializers
from .models import Client, Indication


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class IndicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indication
        fields = '__all__'
        read_only_fields = ['status']
