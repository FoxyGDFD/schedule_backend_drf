from rest_framework import serializers
from ...models import Group as GroupModel
from rest_framework_recursive.fields import RecursiveField


class Group(serializers.ModelSerializer):
    subgroups = RecursiveField(many=True, required=False)

    class Meta:
        model = GroupModel
        fields = "__all__"