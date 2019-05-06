from django.contrib import admin
from ..models.station import Station


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    pass
