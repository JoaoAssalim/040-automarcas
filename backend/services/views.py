from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from backend.models import Part, Service

def delete_part(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    
    if request.method == "POST":
        part_name = part.part_name
        part.delete()
        messages.success(request, f"A peça '{part_name}' foi deletada com sucesso.")
        return redirect(reverse('pecas-list'))
    
    return redirect(reverse('pecas-list'))

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == "POST":
        service_name = f"{service.vehicle_brand} {service.vehicle_model}"
        service.delete()
        messages.success(request, f"O serviço para '{service_name}' foi deletado com sucesso.")
        return redirect(reverse('services-list'))
    
    return redirect(reverse('services-list'))