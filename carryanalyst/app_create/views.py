from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizer import AppointmentSerializer
from .models import Hall,Appointment
from datetime import datetime

class AppointmentListiew(APIView):
    def get(self,request):
          ap_capacity = self.request.GET.get('capacity')
          ap_date = self.request.GET.get('date')
          ap_time = self.request.GET.get('time')
          ap_hall = self.request.GET.get('hall')
          start_date = self.request.GET.get('start_date')
          end_date = self.request.GET.get('end_date')

          print(ap_time, ap_date, ap_capacity,ap_hall)
          one = ''
          date_object=datetime.now()
          app_none=Appointment.objects.none()
          serilizer = AppointmentSerializer(app_none, many=True)
          if ap_capacity and ap_date and ap_time and not ap_hall:
              date_object = datetime.strptime(ap_date, '%m-%d-%Y').date()
              hall_objs = Hall.objects.all()
              for i in hall_objs:
                  if i.capacity >= int(ap_capacity) and i.is_active == 0:
                      one = i

                      break
              hall_inst= Hall.objects.get(name=one)
              app = Appointment(date=date_object, time=ap_time, hall=hall_inst) #instance
              app.save()
              app1=Appointment.objects.filter(date=date_object, time=ap_time)
              serilizer=AppointmentSerializer(app1, many=True) #instance cannot be passed
          elif ap_capacity and ap_date and ap_time and ap_hall:
              date_object = datetime.strptime(ap_date, '%m-%d-%Y').date()
              app2=Appointment.objects.get(date=date_object, time=ap_time)
              print(ap_hall.upper())
              if ap_hall.upper()==str(app2.hall.name):
                  hall_instance=Hall.objects.get(name=app2.hall.name)
                  hall_instance.is_active=1
                  hall_instance.save()
                  app2.booked = 1
                  app2.save()

                  app3=Appointment.objects.filter(date=date_object, time=ap_time)
                  serilizer = AppointmentSerializer(app3, many=True)
          elif start_date and end_date:
              print(start_date)
              print(end_date)
              start_date_object = datetime.strptime(start_date, '%m-%d-%Y').date()
              end_date_object = datetime.strptime(end_date, '%m-%d-%Y').date()
              app4 = Appointment.objects.filter(date__gte=start_date_object, date__lte=end_date_object)
              serilizer = AppointmentSerializer(app4, many=True)

          return Response(serilizer.data)




          #return app
    # #     print("abc")
    # #     # print("capacity::::::::::::::::::::::::::::::::::::::::::::", ap_capacity)
    # #     # print("date::::::::::::::::::::::::::::::::::::::::::::", ap_date)
    # #     # print("time::::::::::::::::::::::::::::::::::::::::::::", ap_time)
    #
    # #
    # #     return app
    #
