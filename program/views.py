from rest_framework import viewsets
from program.models import Client, Indication
from program.serializers import ClientSerializer, IndicationSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class IndicationViewSet(viewsets.ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer