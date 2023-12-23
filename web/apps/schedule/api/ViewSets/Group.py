from rest_framework import viewsets
from apps.schedule.models import Group as GroupModel
from apps.schedule.api.Serializers import Group as GroupSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class Group(viewsets.ModelViewSet):
    '''
    Группа студентов. Группа, имеющая в качестве родителя группу - подгруппа
    '''
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend] 
    search_fields = ['name']
    filterset_fields = ['name']