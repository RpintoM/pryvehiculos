from django.contrib import admin
from apps.vehiculos.models import Vehiculos, TipoVehiculo,Marca

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo','color','placa','marca','tipovehiculo')
    ordering = ('modelo','color','placa','marca','tipovehiculo')
    search_fields = ('modelo','color','placa','marca','tipovehiculo')
    list_filter = ('modelo','color','placa','marca','tipovehiculo')

admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculos,VehiculoAdmin)


