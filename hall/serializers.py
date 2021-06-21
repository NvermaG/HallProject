
from rest_framework import serializers

from .models import hall



class hallserializer(serializers.ModelSerializer):
    class Meta:
        model = hall
        fields = [
        'id',
        'hallName',
        'capacity'
        ]
