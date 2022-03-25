from django.contrib import admin
from .models import (VehicleCategory,Driver,
Vehicle,
ParkingSLots,
Event,
Queue)

# Register your models here.
admin.site.register(VehicleCategory)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(ParkingSLots)
admin.site.register(Event)
admin.site.register(Queue)
