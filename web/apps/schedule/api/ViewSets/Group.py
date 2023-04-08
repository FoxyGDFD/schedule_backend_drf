from rest_framework import viewsets
from apps.schedule.models import Group as GroupModel
from apps.schedule.api.Serializers import Group as GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Group(viewsets.ModelViewSet):
    '''
    Группа студентов. Группа, имеющая в качестве родителя группу - подгруппа
    '''
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]