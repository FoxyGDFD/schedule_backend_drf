from rest_framework import viewsets
from apps.schedule.models import Lesson as LessonModel
from apps.schedule.api.Serializers import Lesson as LessonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Lesson(viewsets.ModelViewSet):
    '''
    Пара
    '''
    queryset = LessonModel.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]