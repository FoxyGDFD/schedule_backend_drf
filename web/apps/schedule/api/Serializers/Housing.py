from rest_framework import serializers
from ...models import Housing as HousingModel


class Housing(serializers.ModelSerializer):
    class Meta:
        model = HousingModel
        fields = '__all__'