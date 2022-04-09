from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class VehicleCategory(models.Model):
    VEHICLE_CHOICES = [
    ('PICKUP', 'PICKUP'),
    ('LORRY', 'LORRY'),
    ('TRANSIST', 'TRANSIST'),
   
]
    vehicle_type = models.CharField(max_length=255,choices=VEHICLE_CHOICES,default="PICKUP")
    

    def __str__(self) -> str:
        return self.vehicle_type


class Driver(models.Model):
    driver_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.driver_name



class Vehicle(models.Model):
    vehicle_plate = models.CharField(max_length=255)
    category_id = models.ForeignKey(VehicleCategory,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.vehicle_plate



class ParkingSLots(models.Model):
    parking_slot_no = models.BigIntegerField()
    parking_slot_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.parking_slot_no)



class Event(models.Model):
    vehicle_category_id = models.ForeignKey(VehicleCategory,on_delete=models.CASCADE)
    time = models.BigIntegerField(default=0)
    laoding = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.vehicle_category_id)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Queue(BaseModel):
    QUEUE_CHOICES = [
    ('PENDING', 'PENDING'),
    ('COMPLETED', 'COMPLETED')
   
]
    vehicle_id = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event,on_delete=models.CASCADE)
    parking_slot_id = models.ForeignKey(ParkingSLots,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(max_length=255,choices=QUEUE_CHOICES,default="PENDING")

    def __str__(self) -> str:
        return str(self.vehicle_id)



@receiver(post_save, sender=Queue, dispatch_uid="create_queue")
def update_stock(sender,created, instance, **kwargs):
    if not created:
        if instance.status == "COMPLETED":
            parkin = ParkingSLots.objects.get(id =  instance.parking_slot_id.id)
            parkin.parking_slot_available = True
            parkin.save()
