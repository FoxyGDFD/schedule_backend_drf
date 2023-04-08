from rest_framework import viewsets
from apps.schedule.models import Cathedra as CathedraModel
from apps.schedule.api.Serializers import Cathedra as CathedraSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Cathedra(viewsets.ModelViewSet):
    '''
    Кафедры
    '''
    queryset = CathedraModel.objects.all()
    serializer_class = CathedraSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]