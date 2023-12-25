from rest_framework import viewsets
from apps.schedule.models import Exam as ExamModel
from apps.schedule.api.Serializers import Exam as ExamSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Exam(viewsets.ModelViewSet):
    '''
    Экзамены
    '''
    queryset = ExamModel.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_and_time', 'classroom__id', 'teacher__id', 'group__id']