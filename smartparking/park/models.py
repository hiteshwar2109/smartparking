
from django.db import models

class ParkingLocation(models.Model):
    name = models.CharField(max_length=255)
    slots = models.IntegerField()

class ParkingSlot(models.Model):
    location = models.ForeignKey(ParkingLocation, on_delete=models.CASCADE)
    slot_number = models.IntegerField()
    is_available = models.BooleanField(default=True)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()