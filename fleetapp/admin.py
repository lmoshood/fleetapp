from django.contrib import admin
from fleetapp.models import Rentals
from fleetapp.models import Vehicle
from fleetapp.models import User
admin.site.site_header = "Fleet Administration"
admin.site.site_title = "Fleet system"
admin.site.index_title = "Fleet Home"
class RentalsAdmin(admin.ModelAdmin):
    list_display = ['client', 'vehicle', 'dateRent', 'returnDate']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicleType', 'plateNum']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'licenseNum', 'email', 'DOB']

# Register your models here.
admin.site.register(Rentals, RentalsAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(User, UserAdmin)
