import http

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from program.models import Client, Indication
from program.serializers import ClientSerializer, IndicationSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class IndicationViewSet(viewsets.ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer

    """
class AcceptIndicationViewSet(viewsets.ModelViewSet):
    queryset = Indication.objects.all()
"""#TODO fix it