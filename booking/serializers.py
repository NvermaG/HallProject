from .models import HallBooking
from rest_framework import serializers

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallBooking
        fields = ['user','hall','required_capacity','booking_date','start_timeing','end_timeing']


class HallRange(serializers.ModelSerializer):
    
    class Meta:
        model = HallBooking
        fields = ['booking_date','day']
