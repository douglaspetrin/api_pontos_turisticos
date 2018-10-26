from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha1',)
    # lookup_field = 'nome' # serve para registros unicos, ex: /Ponto 2/
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(id=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome) # __iexact ignora maiusculo ou minusculo

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

        # return PontoTuristico.objects.filter(aprovado=True)


    def list(self, request, *args, **kwargs):

        # return Response({'teste': '123',})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
        # return Response({'Olá,': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['get', 'post'], detail=True) # detail=True indica que tá pegando a pk, ou seja, ta trabalhando com o recurso e não o endpoint em si.
    def denunciar(self, request, pk=None):
        pass

    # acesso como /recurso/funcao -> /1/denunciar/


    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass


    # associa atracoes a um ponto turistico de uma vez via uma lista.
    # http://127.0.0.1:8000/pontosturisticos/23/associa_atracoes/
    # Ex:  { "ids": [ 2, 3, 4 ] }
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('Ok')