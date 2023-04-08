from rest_framework import viewsets
from apps.schedule.models import Subject as SubjectModel
from apps.schedule.api.Serializers import Subject as SubjectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Subject(viewsets.ModelViewSet):
    '''
    Учебный предмет
    '''
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]