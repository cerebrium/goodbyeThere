from .models import Driver, ScheduledDate, Images, Vehicles, Invoice, managers, VehicleDamages, DeductionType, SupportType, VehicleScheduledDate, DailyMessage, DailyServiceLock, RentalVanLock, DailyServiceLockTwo, InvoiceCounter, DriverHistory, DailyServiceOverride, DailyServiceOverrideTwo, ValidationSheet, ValidationMessage, RentalVanOveride, TrackerClass, ValidationLock, DeletedData, EightHourList, ManagerChangeList, RotaLock, ComplianceVan
from rest_framework import serializers


class managersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = managers
        fields = [
            'user_id',
            'email',
            'name',
            'DBS2',
            'DBS3',
            'DSN1',
            'DEX2',
            'DBS2',
            'DXP1',
            'DRR1',
            'DCF1',
            'DOX2',
            'creationDate'
        ]        
  
class DriverSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Driver
        fields =[
            'driver_id',
            'vanOwner',
            'deleteButton',
            'name',
            'location',
            'email',
            'phone',
            'address',
            'datesList',
            'status',
            'DriverUniqueId',
            'SigningUrlNumber',
            'Signed',
            'vehicle_name',
            'approvedBy',
            'approvedDateAndTime',
            'registration',
            'vtype',
            'complianceCheck',
            'vat',
            'vehicle_list',
            'compliance_list',
            'rentalCheckList',
            'Compliance_Van',
            'offBoard',
            'startList',
            'location_history'
        ]
        
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'invoice_id',
            'driver_id',
            'day',
            'routeType',
            'LWP',
            'LVP',
            'SUP',
            'deductions',
            'fuel'
        ]

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = [
            'vehicle_id',
            'registration',
            'make',
            'model',
            'year',
            'companyOwned',
            'vtype',
            'quotePrice',
            'invoice',
            'offboarded'
        ]

class VehicleDamagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleDamages
        fields = [
            'VehicleDamages_id',
            'driver_id',
            'vehicle_id',
            'statmentOfDamage',
            'dateOfIncident',
            'picturesOfIncident',
            'quotePrice',
            'invoice',
            'name'
        ]

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'driver_id',
            'vehicle_id',
            'image_id',
            'name',
            'countryOfIssue',
            'expiryDate', 
            'dueDate',
            'datePassed',
            'photo',
            'managerApprovedName',
            'managerApprovedDate',
            'imagesLink',
            'verified',
            'driverSigned',
            'points',
            'nextDVLAScreenshot',
            'storageBool'
        ]

class ScheduledDatesSerializer(serializers.HyperlinkedModelSerializer):  
    logIn_time = serializers.TimeField(input_formats= ['%H:%M'])
    logOut_time = serializers.TimeField(input_formats= ['%H:%M'])  
    class Meta:
        model = ScheduledDate
        fields = [
            'date_id',
            'manager_id',
            'name',
            'inOff',
            'route',
            'routeNumber',
            'logIn_time',
            'logOut_time',   
            'location',
            'date',
            'driver_id',
            'mileage',
            'start_mileage',
            'finish_mileage',
            'parcel',
            'parcelNotDelivered',
            'TORH',
            'totalRouteForDay',
            'week_number',
            'manager_movement'
        ]

class DeductionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeductionType
        fields = [  
            'deduction_id',
            'date_id',
            'name',
            'amount',
            'comment',
            'date',
            'week_number'
        ]

class SupportTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupportType
        fields = [  
            'support_id',
            'date_id',
            'name',
            'amount',
            'comment',
            'date',
            'week_number'
        ]

class VehicleScheduledDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleScheduledDate
        fields = [  
            'manager_id',
            'vehicleDate_id',
            'vehicle_id',
            'driver_id',
            'date',
            'week_number',
            'location',
            'registration',
            'manager_movement',
            'vtype'
        ]

class DailyMessageSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = DailyMessage
        fields = [
            'message_id',
            'date',
            'message',
            'name',
            'station',
            'dateSubmit'
        ]
class ValidationMessageSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = ValidationMessage
        fields = [
            'message_id',
            'date',
            'message',
            'name',
            'station',
            'week_number',
            'foreignKey'
        ]

class DailyServiceLockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailyServiceLock
        fields = [
            'service_id',
            'date'
        ]
class DailyServiceLockTwoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailyServiceLockTwo
        fields = [
            'service_id',
            'date'
        ]

class DailyServiceOverrideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailyServiceOverride
        fields = [
            'service_id',
            'date'
        ]

class RentalVanOverideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RentalVanOveride
        fields = [
            'service_id',
            'date'
        ]

class DailyServiceOverrideSerializerTwo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailyServiceOverrideTwo
        fields = [
            'service_id',
            'date'
        ]

class ValidationLockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ValidationLock
        fields = [
            'validation_id',
            'date',
            'overriden'
        ]

class InvoiceCounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceCounter
        fields = [
            'invoice_id',
            'current_index'
        ]

class RentalVanLockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RentalVanLock
        fields = [
            'rental_id',
            'date'
        ]

class DriverHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriverHistory
        fields = [
            'DriverHistory_id',
            'date',
            'week_number',
            'driver_id',
            'name',
            'registration',
            'endDate'
        ]

class TrackerClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackerClass
        fields = [
            '_id',
            'date',
            'manager_id',
            'logOut_time',
            'logIn_time',
            'pages_list',
            'latitude',
            'longitude'
        ]

class ValidationSheetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ValidationSheet
        fields = [
            'manager_id',
            'validationSheet_id',
            'date',
            'week_number',
            'routes',
            'support',
            'miles',
            'totalLwp',
            'totalLVP',
            'totalTraining',
            'R2',
            'R4',
            'R6',
            'Missortfourth',
            'Missortsixth',
            'DpmoBonus',
            'station',
            'Jumper',
            'manager_movement'
        ]

class DeletedDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeletedData
        fields = [
            '_id',
            'date',
            'manager_id',
            'deletion_info'
        ]

class EightHourListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EightHourList
        fields = [
            '_id',
            'date',
            'locktype',
            'lockid',
            'current_date'
        ]

class ManagerChangeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManagerChangeList
        fields = [
            '_id',
            'date',
            'week_number',
            'station',
            'driver_id'
        ]

class RotaLockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RotaLock
        fields = [
            'validation_id',
            'date',
            'week_number',
            'overriden'
        ]

class ComplianceVanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComplianceVan
        fields = [
            'Compliance_Van_Id',
            'Assighned_Date',
            'Returned_Date',
            'Driver_Id',
            'vehicle_Id',
            'next'
        ]


