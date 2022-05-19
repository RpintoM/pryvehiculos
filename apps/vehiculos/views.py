from django.shortcuts import render, redirect
from apps.vehiculos.formVehiculo import VehiculoForm
from apps.vehiculos.models import Vehiculos

# Create your views here.

def listVehiculos(request):
    vehiculos = Vehiculos.objects.all().order_by('-id')
    context ={'vehiculos':vehiculos}
    return render(request, 'vehiculos/listVehiculos.html',context)
    
def home (request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos')
    else:
        form = VehiculoForm()
        return render(request,'vehiculos/vehiculo_form.html', {'form': form})
    
def vehiculoEdit(request, id_vehiculo):
    vehiculo = Vehiculos.objects.get(pk=id_vehiculo)
    
    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculo)
    else:
        form=VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listVehiculos')
    return render(request,'vehiculos/vehiculo_form.html', {'form': form})

def vehiculoEliminar(request, id_vehiculo):
    vehiculo= Vehiculos.objects.get(pk=id_vehiculo)
    
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculos:listVehiculos')
    return render(request, 'vehiculos/vehiculoEliminar.html', {'vehiculo': vehiculo})
    
    
    
    