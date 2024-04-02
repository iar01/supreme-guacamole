from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    floor_name = models.CharField(max_length=50)
    floor_planning = models.ImageField(upload_to='floor', null=True, blank=True)

    def __str__(self):
        return self.building.name + "-" + self.floor_name + "-" + str(self.floor_number)

    class Meta:
        ordering = ['id']


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    is_bookable = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name + "" + str(self.room_number)

    class Meta:
        ordering = ['id']

    def is_available(self, start_time, end_time):
        existing_bookings = Booking.objects.filter(room=self).filter(
            Q(start_time__lte=end_time, end_time__gte=start_time)
        )
        return not existing_bookings.exists()


class Booking(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
