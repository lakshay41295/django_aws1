from rest_framework import serializers
from .models import  Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    hall_name=serializers.SerializerMethodField()
    conform_status=serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = ('appointment_id', 'date', 'time','hall_name','conform_status')

    def get_hall_name(self, obj):
        hall_name=obj.hall.name
        return  hall_name

    def get_conform_status(self,obj):
        if obj.booked==1:
            return "confirm "
        else:
            return "not confirm"
