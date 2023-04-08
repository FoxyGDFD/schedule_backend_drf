from rest_framework import viewsets
from apps.schedule.models import Faculty as FacultyModel
from apps.schedule.api.Serializers import Faculty as FacultySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Faculty(viewsets.ModelViewSet):
    '''
    Факультеты
    '''
    queryset = FacultyModel.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]