from django.urls import path, include
from .viewsets import router
from .views.stations import get_stations, get_station


urlpatterns = [
    path('', include(router.urls)),
    path('stations', get_stations, name='stations'),
    path('stations/<int:id>', get_station, name='station'),
]
