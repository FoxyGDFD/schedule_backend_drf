from rest_framework import viewsets
from apps.schedule.models import Direction as DirectionModel
from apps.schedule.api.Serializers import Direction as DirectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Direction(viewsets.ModelViewSet):
    '''
    Направление обучения
    '''
    queryset = DirectionModel.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]