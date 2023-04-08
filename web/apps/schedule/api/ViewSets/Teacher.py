from rest_framework import viewsets
from apps.schedule.models import Teacher as TeacherModel
from apps.schedule.api.Serializers import Teacher as TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Teacher(viewsets.ModelViewSet):
    '''
    Преподаватель
    '''
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]