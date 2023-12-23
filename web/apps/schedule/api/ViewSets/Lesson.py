from rest_framework import viewsets
from apps.schedule.models import Lesson as LessonModel
from apps.schedule.api.Serializers import Lesson as LessonSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class Lesson(viewsets.ModelViewSet):
    '''
    Пара
    '''
    queryset = LessonModel.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['week_day', 'classroom__id', 'teacher__id', 'group__id']