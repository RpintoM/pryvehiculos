from django import forms
from apps.vehiculos.models import Vehiculos

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculos
        #Es una lista
        fields = [
            'modelo',
            'color',
            'placa',
            'motor',
            'marca',
            'tipovehiculo',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'modelo': 'Ingrese el modelo',
            'color': 'Ingrese el color',
            'placa': 'Ingrese la placa',
            'motor': 'Ingrese el motor',
            'marca': 'Ingrese la marca',
            'tipovehiculo': 'Ingrese el tipo del vehiculo',
        }

        widgets ={
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'tipovehiculo': forms.Select(attrs={'class': 'form-control'}),
        }