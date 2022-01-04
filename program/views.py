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

"""class MainPage(APIView):
    http_method_names = ['get']
    
    #Description of routes according to the desired action
    #Each route will be detailed in the urls.py layer


    def get(self, request):
        urls = {'Cadastro': 'client/',
                'Indication': 'create-indication/',
                }
        return Response(urls, status=http.HTTPStatus.OK)
""""""
class CreateIndication(APIView):
    serializer_class = IndicationSerializer
    http_method_names = ['post', ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.data['indicated_cpf'] :
                with transaction.atomic():
                    serializer.save()
                    indication = Indication.objects.create(indication_user_id=request.data['source_cpf'], )
                    indication.save()
                return Response({'Indicação cadastrada': serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'Erro': "O cliente não pode indicar a si mesmo"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    """