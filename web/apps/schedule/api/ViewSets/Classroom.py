from rest_framework import viewsets
from apps.schedule.models import Classroom as ClassroomModel
from apps.schedule.api.Serializers import Classroom as ClassroomSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class Classroom(viewsets.ModelViewSet):
    '''
    Аудитории
    '''
    queryset = ClassroomModel.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend] 
    search_fields = ['name']
    filterset_fields = ['name']