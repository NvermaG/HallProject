from django.shortcuts import render
from booking.serializers import HallSerializer,HallRange
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import HallBooking
from hall.models import hall
from django.http import HttpResponse
import django_filters.rest_framework
import django_filters
import datetime

# Create your views here.


class BookingView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = HallSerializer
    queryset = HallBooking.objects.all()
    http_method_names = ["get", "post", "put", "delete"]


    def list(self, request):
        obj = HallBooking.objects.all()
        serializer = HallSerializer(obj,many=True)
        return Response(serializer.data)

    def create(self,request):

        serializer = HallSerializer(data=request.data)
        serializer.is_valid()
        halldata = hall.objects.all()
        bookingdata = HallBooking.objects.all()
        req_date = []
        req_time = []
        req_endtime =[]
        strength = 0
        halllist = []
        capacitylist = []
        hall_name = str(serializer.validated_data.get('hall'))
        seat = int(serializer.validated_data.get('required_capacity'))
        date = serializer.validated_data.get('booking_date')
        start_time = serializer.validated_data.get('start_timeing')
        end_time = serializer.validated_data.get('end_timeing')
        pos = 0
        ref_pos = 0
        rd = 0
        rt = 0
        re = 0

        for i in halldata:
            halllist.append(str(i.hallName))
            capacitylist.append(int(i.capacity))

        # for i in bookingdata:
            # if str(i.hall)

        for i in range(0,len(halllist)-1):
            if hall_name == halllist[i]:
                ref_pos = i+1
                break

        for i in range(0,len(capacitylist)-1):
            if capacitylist[ref_pos] >= seat:
                pass
            if capacitylist[ref_pos] <= seat:
                ref_pos+=1


        for i in bookingdata:
            if str(i.hall) == hall_name:
                d = str(i.booking_date)
                t = str(i.start_timeing)
                e = str(i.end_timeing)
                req_date.append(d)
                req_time.append(t)
                req_endtime.append(e)


            if str(i.hall) == halllist[ref_pos]:
                rd = str(i.booking_date)
                rt = str(i.start_timeing)
                re = str(i.end_timeing)
        count = 0

        if str(date) == rd:
            ref_pos = ref_pos + 1


        for i in halldata:
            if i.hallName == hall_name:
                strength = i.capacity
                name = i.hallName

        if strength < seat:
            return HttpResponse("Hall is too small go for Another Hall {}".format(halllist[ref_pos]))

        for i in req_date:
            pos+=1
            if str(date) == i:
                count = pos
                if str(start_time) == req_time[count-1]:
                    return HttpResponse("Hall already Booked refer {}".format(halllist[ref_pos]))

                elif str(start_time) < req_endtime[count-1]:
                    return HttpResponse("Hall already Booked")

        # print(serializer.validated_data.get('hall'))
        serializer.save()
        return Response(serializer.data)


    def update(self,request,*args, **kwargs):

        instance = self.get_object()
        data = request.data
        serializer = HallSerializer(instance,data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response("Object updated")


class BookingList(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = HallBooking.objects.all()


    def listrange(self, request):
        start_date = "2021-07-1"
        end_date = "2021-08-25"
        obj = HallBooking.objects.filter(booking_date__gte=start_date).filter(booking_date__lte=end_date)
        serializer = HallRange(obj,many=True)

        return Response(serializer.data)
