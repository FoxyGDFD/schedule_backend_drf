from rest_framework import viewsets
from apps.schedule.models import DirectionTrainingType as DirectionTrainingTypeModel
from apps.schedule.api.Serializers import DirectionTrainingType as DirectionTrainingTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DirectionTrainingType(viewsets.ModelViewSet):
    '''
    Тип подготовки на направлении подготовки. (Бакалавриат, Специалитет, Магистратура...)
    '''
    queryset = DirectionTrainingTypeModel.objects.all()
    serializer_class = DirectionTrainingTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]