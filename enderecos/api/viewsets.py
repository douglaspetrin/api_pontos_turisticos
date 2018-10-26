from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing Endereço.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer