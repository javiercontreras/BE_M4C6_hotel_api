from rest_framework import serializers
from .models import Room, Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'description', 'price_per_night', 'is_available']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'room', 'guser', 'check_in', 'check_out']
        