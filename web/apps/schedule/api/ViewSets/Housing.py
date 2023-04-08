from rest_framework import viewsets
from apps.schedule.models import Housing as HousingModel
from apps.schedule.api.Serializers import Housing as HousingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Housing(viewsets.ModelViewSet):
    '''
    Учебный корпус
    '''
    queryset = HousingModel.objects.all()
    serializer_class = HousingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]