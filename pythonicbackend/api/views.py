from .models import Driver, ScheduledDate, DriverManager, ScheduledDatesManager, Images, Vehicles, Invoice, managers, VehicleDamages, SupportType, DeductionType
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import managersSerializer, DriverSerializer, ScheduledDatesSerializer, ImagesSerializer, VehiclesSerializer, InvoiceSerializer, VehicleDamagesSerializer, SupportTypeSerializer, DeductionTypeSerializer
from .functions import timeDifference, returnOrderdData, statistics, invoice
from .test_data import importData
import csv, io 


class managersViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    # Users
    queryset = managers.objects.all()
    serializer_class = managersSerializer

class DriverViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer

class InvoicesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
        
class ImagesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class VehicleDamagesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = VehicleDamages.objects.all()
    serializer_class = VehicleDamagesSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    # schedule
    queryset = ScheduledDate.objects.all().order_by('driver_id')
    serializer_class = ScheduledDatesSerializer

class DataViewSet(APIView):
    # Authentication
    permission_classes = (IsAuthenticated,)
   

    # function for all data
    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        images = Images.objects.all()
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': returnOrderdData(drivers, schedule, images, vehicles, deductions, support)
        }
        return Response(content)

class InvoiceViewSet(APIView):
        # function for all data
    def get(self, request):
        # defining overall data objects
        invoices = Invoice.objects.all()
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': invoice(drivers, schedule, vehicles, deductions, support)
        }
        return Response(content)

class StatisticsViewSet(APIView):
    permission_classes = (IsAuthenticated,)
   

    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        images = Images.objects.all()

        content = {
            'data': statistics(schedule)
        }

        return Response(content)

class MapViewSet(APIView):
    # Authentication
    permission_classes = (IsAuthenticated,)
 
    # This route is just a route that allows us to call the function in the test_data.py file with the correct environment  

    # function for all data
    def get(self, request):
        content = {
            'data': importData(ScheduledDate, Driver, DriverManager, ScheduledDatesManager) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class SupportViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = SupportType.objects.all()
    serializer_class = SupportTypeSerializer

class DeductionViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DeductionType.objects.all()
    serializer_class = DeductionTypeSerializer
