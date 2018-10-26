from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing Comentários.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer