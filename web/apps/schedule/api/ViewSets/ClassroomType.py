from rest_framework import viewsets
from apps.schedule.models import ClassroomType as ClassroomTypeModel
from apps.schedule.api.Serializers import ClassroomType as ClassroomTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ClassroomType(viewsets.ModelViewSet):
    '''
    Типы аудиторий. (Компьютерная, лекционная...)
    '''
    queryset = ClassroomTypeModel.objects.all()
    serializer_class = ClassroomTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]