from .models import Driver, ScheduledDate, DriverManager, ScheduledDatesManager, Images, Vehicles, Invoice, managers, VehicleDamages, SupportType, DeductionType, VehicleScheduledDate, DailyMessage, DailyServiceLock, RentalVanLock, DailyServiceLockTwo, InvoiceCounter, DriverHistory, DailyServiceOverride, DailyServiceOverrideTwo, ValidationSheet
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import viewsets
import json
import base64
from rest_framework.permissions import IsAuthenticated
from .serializers import managersSerializer, DriverSerializer, ScheduledDatesSerializer, ImagesSerializer, VehiclesSerializer, InvoiceSerializer, VehicleDamagesSerializer, SupportTypeSerializer, DeductionTypeSerializer, VehicleScheduledDateSerializer, DailyMessageSerializer, DailyServiceLockSerializer, RentalVanLockSerializer, DailyServiceLockTwoSerializer, InvoiceCounterSerializer, DriverHistorySerializer, DailyServiceOverrideSerializer, DailyServiceOverrideSerializerTwo, ValidationSheetSerializer
from .functions import timeDifference, returnOrderdData, statistics, invoice, returnVanOrderedData, tokenizer, complianceCheck, addDatedDriver, documentsDriversOnly, dailyService, vanWeeklyDates
from .test_data import importData
import csv, io 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db.models import Q
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize


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

class VehicleScheduledDateViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = VehicleScheduledDate.objects.all()
    serializer_class = VehicleScheduledDateSerializer

class VehicleMapViewSet(APIView):

    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all()
        theDate = request.body

        content = {
            'data': returnVanOrderedData(vehicles, vehiclesDates, images, drivers, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all()
        content = {
            'data': returnVanOrderedData(vehicles, vehiclesDates, images, drivers) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class InvoiceViewSet(APIView):
    # function for all data
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theDate = body['date']
        theWeek = body['week']
        drivers = Driver.objects.all()
        
        # filtered queries
        schedule = ScheduledDate.objects.filter(Q(week_number = theWeek))
        deductions = DeductionType.objects.filter(Q(week_number = theWeek))
        support = SupportType.objects.filter(Q(week_number = theWeek))

        drivers = Driver.objects.all().order_by('name')

        # vehicles = Vehicles.objects.all()

        content = {
            'data': invoice(drivers, schedule, deductions, support, theDate)
        }
        return Response(content)   

    def get(self, request):
        # defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': invoice(drivers, schedule, vehicles, deductions, support)
        }
        return Response(content)

class DailyServiceViewSet(APIView):
    # function for all data
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theDate = body['date']
        theWeek = body['week']
        drivers = Driver.objects.all()
        
        # filtered queries
        schedule = ScheduledDate.objects.filter(Q(week_number = theWeek))
        deductions = DeductionType.objects.filter(Q(week_number = theWeek))
        support = SupportType.objects.filter(Q(week_number = theWeek))

        drivers = Driver.objects.all().order_by('name')

        content = {
            'data': dailyService(drivers, schedule, deductions, support, theDate)
        }
        return Response(content)   

    def get(self, request):
        # defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': dailyService(drivers, schedule, deductions, support)
        }
        return Response(content)

class securityViewSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        managerList = managers.objects.all()

        return Response({
            'token': tokenizer(managerList, request.body)
        })

class ComplianceMapViewSet(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all()
        theDate = request.body

        content = {
            'data': complianceCheck(vehicles, vehiclesDates, images, drivers, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all()
        content = {
            'data': complianceCheck(vehicles, vehiclesDates, images, drivers) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class AutoSchedulingMapViewSet(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theDate = body['date']
        theWeek = body['week']
        theNextWeek = theWeek+1
        drivers = Driver.objects.all()
        
        # schedule = ScheduledDate.objects.all()
        schedule = ScheduledDate.objects.filter(Q(week_number = theWeek) | Q(week_number = theNextWeek))

        content = {
            'data': addDatedDriver(drivers, schedule, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        content = {
            'data': addDatedDriver(drivers, schedule) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class docDrivers(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,) 

    def post(self, request): 
        drivers = Driver.objects.all().order_by('driver_id')
        images = Images.objects.all().order_by('driver_id')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        station = body['station']

        content = {
            'data': documentsDriversOnly(drivers, images, station) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)


        # function for all data
    def get(self, request):
        drivers = Driver.objects.all().order_by('driver_id')
        images = Images.objects.all().order_by('driver_id')
        content = {
            'data': documentsDriversOnly(drivers, images) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class VanWeeklyDatesView(APIView):

            # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        theNextWeek = theWeek+1
        
        dates = VehicleScheduledDate.objects.filter(Q(week_number = theWeek))
        serializer = VehicleScheduledDateSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

        # Authentication
    # permission_classes = (IsAuthenticated,)

    # serializer_class = VehicleScheduledDateSerializer
    # def post(self, request):
    #     body_unicode = request.body.decode('utf-8')
    #     body = json.loads(body_unicode)
    #     date = body['date']
    #     theWeek = body['week']
    #     vehicleDates = VehicleScheduledDate.objects.filter(Q(week_number = theWeek))

    #     content = {
    #         'data': vanWeeklyDates(vehicleDates, date)
    #     }
    #     return Response(content)
    
class DailyMessageViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DailyMessage.objects.all()
    serializer_class = DailyMessageSerializer

class DailyServiceLockViewSet(viewsets.ModelViewSet):
        # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = RentalVanLock.objects.all()
    serializer_class = DailyServiceLockSerializer

class DailyServiceLockTwoViewSet(viewsets.ModelViewSet):
        # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DailyServiceLockTwo.objects.all()
    serializer_class = DailyServiceLockTwoSerializer

class DailyServiceOverrideViewSet(viewsets.ModelViewSet):
        # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DailyServiceOverride.objects.all()
    serializer_class = DailyServiceOverrideSerializer

class DailyServiceOverrideTwoViewSet(viewsets.ModelViewSet):
        # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DailyServiceOverrideTwo.objects.all()
    serializer_class = DailyServiceOverrideSerializerTwo

class RentalVanLock(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = RentalVanLock.objects.all()
    serializer_class = RentalVanLockSerializer

class ReturnScheduledSorts(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        theNextWeek = theWeek+1
        
        dates = ScheduledDate.objects.filter(Q(week_number = theWeek) | Q(week_number = theNextWeek))
        serializer = ScheduledDatesSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnScheduledSingleSorts(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        theDate = body['date']
        
        dates = ScheduledDate.objects.filter(Q(week_number = theWeek), Q(date = theDate))
        serializer = ScheduledDatesSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnScheduledSortWeek(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        
        dates = ScheduledDate.objects.filter(Q(week_number = theWeek))
        serializer = ScheduledDatesSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnDeductionsSort(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        
        dates = DeductionType.objects.filter(Q(week_number = theWeek))
        serializer = DeductionTypeSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnSupportSort(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        
        dates = SupportType.objects.filter(Q(week_number = theWeek))
        serializer = SupportTypeSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnDriverImage(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        driver_id = body['driver_id']
        
        dates = Images.objects.filter(Q(driver_id = driver_id))
        serializer = ImagesSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ReturnInvoiceNumber(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = InvoiceCounter.objects.all()
    serializer_class = InvoiceCounterSerializer

class DriverHistoryAddView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = DriverHistory.objects.all()
    serializer_class = DriverHistorySerializer

class DriverHistoryView(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theVID = body['vehicle_id']
        
        dates = DriverHistory.objects.filter(Q(registration = theVID))
        serializer = DriverHistorySerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ValidationSheetView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = ValidationSheet.objects.all()
    serializer_class = ValidationSheetSerializer


class ValidationSheetSort(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        
        dates = ValidationSheet.objects.filter(Q(week_number = theWeek))
        serializer = ValidationSheetSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})

class ValidationSheetSortTwo(APIView):
        # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theWeek = body['week']
        
        dates = ValidationSheet.objects.filter(Q(week_number = theWeek))
        serializer = ValidationSheetSerializer(dates, many=True, context={'request': request})

        return Response({"data": serializer.data})