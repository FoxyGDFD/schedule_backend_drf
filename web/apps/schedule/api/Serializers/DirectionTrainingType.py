from rest_framework import serializers
from ...models import DirectionTrainingType as DirectionTrainingTypeModel


class DirectionTrainingType(serializers.ModelSerializer):
    class Meta:
        model = DirectionTrainingTypeModel
        fields = '__all__'