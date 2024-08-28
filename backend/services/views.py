from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from backend.models import Part, Service

def delete_part(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    
    if part:
        part_name = part.part_name
        part.delete()
        messages.success(request, f"A peça '{part_name}' foi deletada com sucesso.")
    
    return redirect(reverse('pecas-list'))

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if service:
        service_name = f"{service.brand} {service.model}"
        service.delete()
        messages.success(request, f"O serviço para '{service_name}' foi deletado com sucesso.")
    
    return redirect(reverse('services-list'))
    
def create_service(request):
    brand = request.POST.get('vehicleBrand')
    model = request.POST.get('vehicleModel')
    license_plate = request.POST.get('vehiclePlate')
    year = request.POST.get('vehicleYear')
    owner_name = request.POST.get('ownerName')
    owner_phone = request.POST.get('phoneNumber')
    problem_description = request.POST.get('problemDescription')
    
    service = Service(
        brand=brand,
        model=model,
        license_plate=license_plate,
        year=year,
        owner_name=owner_name,
        owner_phone=owner_phone,
        problem_description=problem_description
    )
    service.save()

    return redirect(reverse('services-list'))

def create_part(request):
    part_name = request.POST.get('partName')
    part_code = request.POST.get('partCode')
    manufacturer = request.POST.get('manufacturer')
    vehicle_compatibility = request.POST.get('vehicleCompatibility')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    supplier = request.POST.get('supplier')
    purchase_date = request.POST.get('purchaseDate')
    additional_info = request.POST.get('description')
    
    print(
        part_name,
        part_code,
        manufacturer,
        vehicle_compatibility,
        quantity,
        price,
        supplier,
        purchase_date,
        additional_info
    )
    
    part = Part(
        part_name=part_name,
        part_code=part_code,
        manufacturer=manufacturer,
        vehicle_compatibility=vehicle_compatibility,
        quantity=quantity,
        price=price,
        supplier=supplier,
        purchase_date=purchase_date,
        additional_info=additional_info
    )
    part.save()

    return redirect(reverse('pecas-list'))