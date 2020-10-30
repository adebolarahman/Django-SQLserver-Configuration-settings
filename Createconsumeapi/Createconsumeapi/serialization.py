from rest_framework import serializers
from Createconsumeapi.models import Empmodel


class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Empmodel
        fields='__all__'