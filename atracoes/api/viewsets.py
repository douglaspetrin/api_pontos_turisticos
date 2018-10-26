from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

from django_filters import rest_framework as filters



class AtracaoFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name="nome", lookup_expr='icontains')
    descricao = filters.CharFilter(field_name="descricao", lookup_expr='icontains')
    horario_func = filters.CharFilter(field_name="horario_func", lookup_expr='icontains')
    idade_min = filters.CharFilter(field_name="idade_min", lookup_expr='icontains')

    class Meta:
        model = Atracao
        fields = ['nome','descricao','horario_func', 'idade_min',]


class AtracaoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    # filter_fields = ('nome', 'descricao',)

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AtracaoFilter