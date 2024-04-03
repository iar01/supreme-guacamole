from rest_framework import serializers
from .models import *


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    building = BuildingSerializer()

    class Meta:
        model = Floor
        fields = '__all__'


class TimeSlot(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    floor = FloorSerializer()
    booked_slots = TimeSlot(many=True)

    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
