from djmoney.models.fields import MoneyField
import locale
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django import forms
from django.utils import timezone
import pytz

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
    creationDate = models.CharField(max_length = 50, default = datetime.date.today())

class DriverManager(models.Manager):
    def create_driver(self, name):
        driver = self.create(name=name)

        return driver
        
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True, unique=True) #need to connect to DA Compliance Check
    vehicle_name = models.CharField(max_length=50, null = True)
    deleteButton = models.CharField(max_length = 100, null=True)

    #the following fields will be displayed when a manager clicks on "Add Driver"
    name = models.CharField(max_length = 100, null = True)
    location = models.CharField(max_length = 15, default = 'DBS2', null = True) #want to change to depot
    email = models.CharField(max_length = 50, null=True)
    phone = models.CharField(max_length = 20, null=True)
    address = models.CharField(max_length=100, null=True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    status = models.CharField(max_length = 30, null = True)
    DriverUniqueId = models.CharField(max_length = 30, null=True)
    SigningUrlNumber = models.CharField(max_length = 100, null=True)
    Signed = models.BooleanField(default=False)
    approvedBy = models.CharField(max_length = 30, null=True)
    approvedDateAndTime = models.CharField(max_length = 100, null=True)
    vanOwner = models.BooleanField(default=False)
    registration = models.CharField(max_length = 30, null=True)
    vtype = models.CharField(max_length = 30, null=True)
    complianceCheck = models.CharField(max_length = 30, null=True)

    objects = DriverManager() # allows us to call method above
    #week = models.DateField("week", default = datetime.date.today.isocalendar()[1])
    
    def __str__(self):
        return self.name 

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
    logOut_time = models.TimeField("LOG OUT", null = True)
    logIn_time = models.TimeField("LOG IN", null = True)

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
    vehicleDate_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    vehicle_id = models.ForeignKey(Vehicles, null=True, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())

class DeductionType(models.Model):
    deduction_id = models.AutoField(primary_key=True, unique=True)
    date_id = models.ForeignKey(ScheduledDate, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 500)
    amount = MoneyField("Deduction", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
   
    def __str__(self):
        return self.name

class SupportType(models.Model):
    support_id = models.AutoField(primary_key=True, unique=True)
    date_id = models.ForeignKey(ScheduledDate, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    comment = models.CharField(max_length = 500)
    amount = MoneyField("Support", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    def __str__(self):
        return self.name

 