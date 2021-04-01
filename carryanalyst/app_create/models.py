from django.db import models
from django.utils import timezone
# Create your models here.
class Hall(models.Model):
    """
       This model is used to intilize halls where is active 0-> not boocked  and 1-> booked
     """
    name = models.CharField(null=False, blank=False,max_length=100)
    capacity = models.PositiveIntegerField(null=False, blank=True , default=0)
    is_active = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Hall"

    def __str__(self):
        return self.name



class Appointment(models.Model):
    """
       This model is used to intilize halls where booked  0-> not boocked  and 1-> booked
     """

    appointment_id=models.AutoField(primary_key=True, default=0 )
    date = models.DateField(null=False,blank=False)
    time = models.CharField(max_length=200, null=False,blank=False, default='')


    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked=models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Appointment"

    def __str__(self):
        return str(self.appointment_id)



 #presave

