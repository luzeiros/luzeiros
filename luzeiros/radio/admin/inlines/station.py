from django.contrib import admin
from ...models.station import Station


class StationInline(admin.StackedInline):
    model = Station
    extra = 1
