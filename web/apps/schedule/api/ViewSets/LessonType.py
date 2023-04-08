from rest_framework import viewsets
from apps.schedule.models import LessonType as LessonTypeModel
from apps.schedule.api.Serializers import LessonType as LessonTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LessonType(viewsets.ModelViewSet):
    '''
    Тип пары: Лекция, практика, факультатив...
    '''
    queryset = LessonTypeModel.objects.all()
    serializer_class = LessonTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]