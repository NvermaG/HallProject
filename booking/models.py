from django.db import models
from hall.models import hall
from django.contrib.auth.models import User

# Create your models here.

class HallBooking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hall = models.ForeignKey(hall, on_delete=models.CASCADE, related_name="hall_bookings")
    required_capacity = models.IntegerField()
    booking_date = models.DateField(null=True)
    
    start_timeing = models.TimeField(null=True)
    end_timeing = models.TimeField(null=True)

    def __str__(self):
        return self.user.username
