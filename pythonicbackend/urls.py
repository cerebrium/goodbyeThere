from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from pythonicbackend.api import views

router = routers.DefaultRouter()
router.register(r'managers', views.managersViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'images', views.ImagesViewSet)
router.register(r'vehicles', views.VehiclesViewSet)
router.register(r'vehicledamages', views.VehicleDamagesViewSet)
router.register(r'support', views.SupportViewSet)
router.register(r'deductions', views.DeductionViewSet)
router.register(r'vanDates', views.VehicleScheduledDateViewSet)
router.register(r'dailymessage', views.DailyMessageViewSet)
router.register(r'dailyservicelock', views.DailyServiceLockViewSet)
router.register(r'dailyservicelocktwo', views.DailyServiceLockTwoViewSet)
router.register(r'rentallock', views.RentalVanLock)
router.register(r'invoicecounter', views.ReturnInvoiceNumber)
router.register(r'driveraddhistory', views.DriverHistoryAddView)
router.register(r'dailyserviceoverride', views.DailyServiceOverrideViewSet)
router.register(r'dailyserviceoverridetwo', views.DailyServiceOverrideTwoViewSet)
router.register(r'validationsheet', views.ValidationSheetView)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls), name='rest routes'),
    path('asdjflkasj24dflasd43fhapsdjnfkqjwne2r2oqwiefkasjd43nfkjl4nwe31ofiqwefkjan51dmfnqoweifqk123wjenfaskjdnfasdf/', obtain_auth_token),
    path('data/', views.DataViewSet.as_view(), name='data'),
    path('statistics/', views.StatisticsViewSet.as_view(), name='stats'),
    path('csv/', views.MapViewSet.as_view(), name='csv'),
    path('vandata/', views.VehicleMapViewSet.as_view(), name='vehicles data'),
    path('compliancedata/', views.ComplianceMapViewSet.as_view(), name='driver data'),
    path('autoschedule/', views.AutoSchedulingMapViewSet.as_view(), name='scheduling'),
    path('security/', views.securityViewSet.as_view(), name='data_encrypted'),
    path('invoices/', views.InvoiceViewSet.as_view(), name='invoices'),
    path('docdrivers/', views.docDrivers.as_view(), name='docdrivers'),
    path('dailservice/', views.DailyServiceViewSet.as_view(), name='docdrivers'),
    path('vandatesordered/', views.VanWeeklyDatesView.as_view(), name='van dates ordered'),
    path('weeksschedule/', views.ReturnScheduledSorts.as_view(), name='week schedule data'),
    path('weekschedule/', views.ReturnScheduledSortWeek.as_view(), name='week schedule data'),
    path('deductionschedule/', views.ReturnDeductionsSort.as_view(), name='other name'),
    path('supportschedule/', views.ReturnSupportSort.as_view(), name='other other name'),
    path('driverimages/', views.ReturnDriverImage.as_view(), name='Image with id'),
    path('driverhistory/', views.DriverHistoryView.as_view(), name='drivers associated with van'),
    path('singledriverdates/', views.ReturnScheduledSingleSorts.as_view(), name='drivers associated with van'),
    path('validationsort/', views.ValidationSheetSort.as_view(), name='validation sorted'),
    path('tripledates/', views.ReturnScheduledSortsTriple.as_view(), name='triple week dates')
]
