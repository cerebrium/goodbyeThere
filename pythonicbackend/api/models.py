from djmoney.models.fields import MoneyField
import locale
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django import forms
from django.utils import timezone

class managers(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, 
        editable=False
    )
    email = models.CharField(max_length = 100, unique=True)
    name = models.CharField(max_length = 100, null = True)
    DBS2 = models.BooleanField(default=False)
    DSN1 = models.BooleanField(default=False)
    DEX2 = models.BooleanField(default=False)
    DXP1 = models.BooleanField(default=False)
    DRR1 = models.BooleanField(default=False)
    DCF1 = models.BooleanField(default=False)
    creationDate = models.CharField(max_length = 50, default = datetime.date.today())

class DriverManager(models.Manager):
    def create_driver(self, name):
        driver = self.create(name=name)

        return driver
        
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True, unique=True) #need to connect to DA Compliance Check
    vehicle_name = models.CharField(max_length = 20, null=True)
    vehicle_list = ArrayField(models.CharField(max_length=60), default=list, blank=True)
    deleteButton = models.CharField(max_length = 100, null=True)

    #the following fields will be displayed when a manager clicks on "Add Driver"
    name = models.CharField(max_length = 100, null = True)
    location = models.CharField(max_length = 15, default = 'DBS2', null = True) #want to change to depot
    email = models.CharField(max_length = 50, null=True, unique=True)
    phone = models.CharField(max_length = 20, null=True)
    address = models.CharField(max_length=100, null=True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    rentalCheckList = ArrayField(models.CharField(max_length=25), default=list, blank=True)
    status = models.CharField(max_length = 50, null = True)
    DriverUniqueId = models.CharField(max_length = 30, null=True)
    SigningUrlNumber = models.CharField(max_length = 100, null=True)
    Signed = models.BooleanField(default=False)
    approvedBy = models.CharField(max_length = 30, null=True)
    approvedDateAndTime = models.CharField(max_length = 100, null=True)
    vanOwner = models.BooleanField(default=False)
    registration = models.CharField(max_length = 30, null=True)
    vtype = models.CharField(max_length = 30, null=True)

    compliance_list = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    complianceCheck = models.CharField(max_length = 30, null=True)
    vat = models.BooleanField(default=False)

    objects = DriverManager() # allows us to call method above
    #week = models.DateField("week", default = datetime.date.today.isocalendar()[1])
    
    def __str__(self):
        return str(self.driver_id) 

class InvoiceManager(models.Manager):
    def create_Invoice(self, driver_id, day, routeType, LWP, LVP, SUP, deductions, fuel):
        invoice = self.create(
            driver_id = driver_id,
            day = day,
            routeType =routeType, 
            LWP = LWP,
            LVP = LVP,
            SUP = SUP, 
            deductions = deductions,
            fuel = fuel
            )

        return invoice

class Invoice(models.Model):
    name = models.CharField(max_length = 100, null = True)
    invoice_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    day = models.CharField(max_length = 50, null = True)
    routeType = models.CharField(max_length = 10, null = True)
    LWP = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    SUP = MoneyField("SUP", default=0, max_digits=10, decimal_places=2, default_currency='GBP', null = True)
    deductions = MoneyField("Deductions", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    registration = models.CharField(max_length=20, null=True)
    make = models.CharField(max_length=30, null=True)
    model = models.CharField(max_length=30, null=True)
    year = models.CharField(max_length=10, null=True)
    companyOwned = models.BooleanField(default=False)
    vtype = models.CharField(max_length=20, default='standard')
    quotePrice = MoneyField("RENTAL QUOTE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    invoice = MoneyField("INVOICE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    offboarded = models.BooleanField(default=False, null = True)

    def __str__(self):
        return self.registration

class VehicleDamages(models.Model):
    VehicleDamages_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, null = True)
    driver_id = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    statmentOfDamage = models.CharField(max_length = 2000)
    dateOfIncident = models.CharField(max_length = 100)
    picturesOfIncident = models.CharField(max_length = 200)
    quotePrice = MoneyField("INCIDENT QUOTE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    invoice = MoneyField("INCIDENT INVOICE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

class Images(models.Model):
    driver_id = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicles, blank=True, null=True, on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, null = True)
    countryOfIssue = models.CharField(max_length = 30, null=True)
    expiryDate = models.CharField(max_length = 100, null = True)
    dueDate = models.CharField(max_length = 50, null = True)
    datePassed = models.CharField(max_length=30, null=True)
    photo = models.CharField(max_length=15, null=True)
    managerApprovedName = models.CharField(max_length = 30, null=True)
    managerApprovedDate = models.CharField(max_length = 90, null=True)
    imagesLink = models.CharField(max_length=150, null=True)
    verified = models.CharField(max_length = 20, null = True)
    driverSigned = models.BooleanField(default=False)
    points = models.IntegerField(default = 0, null = True)
    nextDVLAScreenshot = models.CharField(max_length = 50, null = True)
    storageBool = models.BooleanField(default=False)
 
    def __str__(self):
        return self.name 

class ScheduledDatesManager(models.Manager):

    def create_date(self, NAME, IN, ROUTE, LOGIN, LOGOUT, TORH, MILEAGE, PARCEL, SUP, deductions, date, driver_id):
        date = self.create(
            name=NAME,
            inOff=IN,
            route=ROUTE,
            logIn_time=LOGIN,
            logOut_time=LOGOUT,
            TORH=TORH,
            mileage=MILEAGE,
            parcel=PARCEL,
            #LateWavePayment=LWP,
            #LVP=LVP,
            #CRT=CRT,
            #RL=RL,
            support=SUP,
            #fuel=FUEL,
            deductions=deductions,
            date=date,
            driver_id=Driver(driver_id),
        )

        return date
  
class ScheduledDate(models.Model):
    # adding live update
    manager_id = models.CharField(null=True, max_length = 100)
    manager_movement = ArrayField(models.CharField(max_length=120), default=list, blank=True)

    # have to add this
    objects = ScheduledDatesManager()
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null = True)


    # all fields needed for the daily feeling sheet report 
    date_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    name = models.CharField(max_length = 50, null = True)
    inOff = models.IntegerField("IN", default=1, editable=True, null = True)
    route = models.CharField("Route", max_length = 30, default = "0", null = True)
    routeNumber = models.CharField("Route", max_length = 30, default = "0", null = True)
    logOut_time = models.TimeField("LOG OUT", null = True, default = '00:00')
    logIn_time = models.TimeField("LOG IN", null = True, default = '00:00')

    # sorting field
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)

     #here we don't need the manager to enter the station every time, but if he choose a driver from anotehr station
     # the location should be either auto filled, or manually
    location = models.CharField(max_length = 15, default='DBS2', null=True)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())
    mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    start_mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    finish_mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    parcel = models.IntegerField("PARCEL", default=0, editable=True, null = True)
    parcelNotDelivered = models.IntegerField("PARCEL NOT DELIVERED", default=0, editable=True, null = True)
    totalRouteForDay = models.CharField(max_length = 10, default='0', null=True)

    #the following fields are Extra's report fields 
    TORH = models.TimeField("TORH", null = True)

    #the following fields are money DEDUCTION fields 
    objects = ScheduledDatesManager()

    def __str__(self):
        return str(self.date_id)

class VehicleScheduledDate(models.Model):
    manager_id = models.CharField(null=True, max_length = 100)
    manager_movement = ArrayField(models.CharField(max_length=120), default=list, blank=True)
    vehicleDate_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    vehicle_id = models.ForeignKey(Vehicles, null=True, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)
    location = models.CharField(max_length = 15, default='DBS2', null=True)
    registration = models.CharField(max_length = 20, default='DBS2', null=True)
    vtype = models.CharField(max_length = 20, default='Standard', null=True)

class DeductionType(models.Model):
    deduction_id = models.AutoField(primary_key=True, unique=True)
    date_id = models.ForeignKey(ScheduledDate, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    date = models.CharField(null=True, max_length = 30)
    comment = models.CharField(max_length = 500)
    amount = MoneyField("Deduction", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
        # sorting field
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)
   
    def __str__(self):
        return self.name

class SupportType(models.Model):
    support_id = models.AutoField(primary_key=True, unique=True)
    date_id = models.ForeignKey(ScheduledDate, null=True, on_delete=models.CASCADE)
    date = models.CharField(null=True, max_length = 30)
    name = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 500)
    amount = MoneyField("Support", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
        # sorting field
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)

    def __str__(self):
        return self.name

class DailyMessage(models.Model):
    message_id = models.AutoField(primary_key=True, unique=True)
    date = models.CharField(null=True, max_length = 30)
    message = models.CharField(null=True, max_length = 900)
    name = models.CharField(null=True, max_length = 300)
    station = models.CharField(null=True, max_length = 15)
    dateSubmit = models.CharField(null=True, max_length = 50)

    def __str__(self):
        return self.message

class DailyServiceLock(models.Model):
    service_id = models.AutoField(primary_key=True, unique=True)
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.service_id

class ValidationLock(models.Model):
    validation_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ) 
    date = models.CharField(null=True, max_length = 30)
    overriden = models.BooleanField(default=False)

    def __str__(self):
        return self.validation_id

class DailyServiceLockTwo(models.Model):
    service_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.service_id

class DailyServiceOverride(models.Model):
    service_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.service_id

class DailyServiceOverrideTwo(models.Model):
    service_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.service_id

class RentalVanLock(models.Model):
    rental_id = models.AutoField(primary_key=True, unique=True)
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.rental_id

class InvoiceCounter(models.Model):
    invoice_id = models.AutoField(primary_key=True, unique=True)
    current_index = models.IntegerField(default=1, editable=True, null = True)
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.invoice_id

class DriverHistory(models.Model):
    DriverHistory_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)
    endDate = models.CharField(null=True, max_length = 30)
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)
    driver_id = models.CharField(null=True, max_length = 100)
    registration = models.CharField(null=True, max_length = 100)
    name = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.DriverHistory_id

class ValidationSheet(models.Model):
    manager_id = models.CharField(null=True, max_length = 100)
    manager_movement = ArrayField(models.CharField(max_length=120), default=list, blank=True)
    validationSheet_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    station = models.CharField(null=True, max_length = 20)
    date = models.CharField(null=True, max_length = 30)
    routes = models.IntegerField("routes", default=0, editable=True, null = True)
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)
    support = MoneyField("Support", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    miles = models.IntegerField("miles", default=0, editable=True, null = True)
    totalLwp = models.IntegerField("total late wave payment", default=0, editable=True, null = True)
    totalLVP = models.IntegerField("total large vehicle payment", default=0, editable=True, null = True)
    totalTraining = models.IntegerField("training", default=0, editable=True, null = True)
    R2 = models.IntegerField("r2", default=0, editable=True, null = True)
    R4 = models.IntegerField("r4", default=0, editable=True, null = True)
    R6 = models.IntegerField("r6", default=0, editable=True, null = True)
    Missortfourth = models.IntegerField("missort fourth", default=0, editable=True, null = True)
    Missortsixth = models.IntegerField("missort sixth", default=0, editable=True, null = True)
    DpmoBonus = models.IntegerField("dpmo bonus", default=0, editable=True, null = True)
    Jumper = models.IntegerField("Jumper", default=0, editable=True, null = True)

    def __str__(self):
        return self.DriverHistory_id

class ValidationMessage(models.Model):
    message_id = models.AutoField(primary_key=True, unique=True)
    date = models.CharField(null=True, max_length = 30)
    message = models.CharField(null=True, max_length = 900)
    name = models.CharField(null=True, max_length = 300)
    station = models.CharField(null=True, max_length = 15)
    week_number = models.IntegerField("WEEKNUMBER", default=1, editable=True, null = True)

    def __str__(self):
        return self.message

class RentalVanOveride(models.Model):
    service_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)

    def __str__(self):
        return self.service_id

class TrackerClass(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)
    manager_id = models.CharField(null=True, max_length = 100)
    logOut_time = ArrayField(models.CharField(max_length=40), default=list, blank=True)
    logIn_time = ArrayField(models.CharField(max_length=40), default=list, blank=True)
    pages_list = ArrayField(models.CharField(max_length=40), default=list, blank=True)
    submitted_data = ArrayField(models.CharField(max_length=40), default=list, blank=True)
    latitude = models.CharField(null=True, max_length = 40)
    longitude = models.CharField(null=True, max_length = 40)

class DeletedData(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 30)
    manager_id = models.CharField(null=True, max_length = 100)
    deletion_info = ArrayField(models.CharField(max_length=40), default=list, blank=True)

class EightHourList(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    current_date = models.CharField(null=True, max_length = 30)
    date = models.CharField(null=True, max_length = 100)
    locktype = models.CharField(null=True, max_length = 100)
    lockid = models.CharField(null=True, max_length = 100)

class ManagerChangeList(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date = models.CharField(null=True, max_length = 100)
    week_number = models.CharField(null=True, max_length = 10)
    station = models.CharField(null=True, max_length = 20)
    driver_id = models.CharField(null=True, max_length = 100)

class RotaLock(models.Model):
    validation_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ) 
    date = models.CharField(null=True, max_length = 30)
    week_number = models.CharField(null=True, max_length = 10)
    overriden = models.BooleanField(default=False)

    def __str__(self):
        return self.validation_id


    