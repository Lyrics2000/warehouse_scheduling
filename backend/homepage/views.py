
from django.shortcuts import render

from homepage.models import Driver, ParkingSLots, Queue, Vehicle, VehicleCategory,Event

# Create your views here.

def index(request):
    
    if request.method =="POST":
        vehicle_type =  request.POST.get("vehicle_type")
        event_type= request.POST.get("event_type")
        driver_name =  request.POST.get("driver_name")
        number_plate =  request.POST.get("number_plate")

        obj ,created = Driver.objects.get_or_create(driver_name = driver_name)
        vv = VehicleCategory.objects.filter(vehicle_type = vehicle_type).first()
        if event_type== "Loading":
            event = Event.objects.filter(vehicle_category_id = vv,laoding=True).first()
        elif event_type == "Offloading":
            event = Event.objects.filter(vehicle_category_id = vv,laoding=False).first()
        
        vehicle = Vehicle.objects.create(
            vehicle_plate = number_plate,
            category_id = vv,
            driver_id = obj
        )

        filter_quue =Queue.objects.all()
        print(filter_quue)
        if len(filter_quue) > 0:# the system is not new as their are some cars that have been used for loading before
            random_slot = ParkingSLots.objects.filter(parking_slot_available = True).first()
            
            if random_slot:# parking slot available
                slot = ParkingSLots.objects.get(id = random_slot.id)
                slot.parking_slot_available = False
                slot.save()
                queue = Queue.objects.create(
                    vehicle_id = vehicle,
                    event_id = event,
                    parking_slot_id = random_slot
                )
                request.session['queue_id'] = queue.id
            else: # parking slot is full,display error message saying slot is full
                pass

        else:# the system is new else no need to allocate parking slot
            queue = Queue.objects.create(
                    vehicle_id = vehicle,
                    event_id = event
                )
            request.session['queue_id'] = queue.id
        all_queue = Queue.objects.filter(status = "PENDING")
        all_queue_completed = Queue.objects.filter(status = "COMPLETED")

        context ={
            'queue':all_queue,
            'completed':all_queue_completed
        }

        return render(request,'index.html',context)
        





    all_queue = Queue.objects.filter(status = "PENDING")
    all_queue_completed = Queue.objects.filter(status = "COMPLETED")
    context ={
            'queue':all_queue,
            'completed':all_queue_completed
        }
    return render(request,'index.html',context)
