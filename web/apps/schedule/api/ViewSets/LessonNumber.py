from rest_framework import viewsets
from apps.schedule.models import LessonNumber as LessonNumberModel
from apps.schedule.api.Serializers import LessonNumber as LessonNumberSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LessonNumber(viewsets.ModelViewSet):
    '''
    Номер пары. Создается отдельно т.к начало и конец 1й, 2й, 3й, 4й и т.д пар могут отличаться от вуза к вузу.
    Также может отличаться количество пар.
    '''
    queryset = LessonNumberModel.objects.all()
    serializer_class = LessonNumberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]