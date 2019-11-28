from django.urls import path, include
from .viewsets.router import router


urlpatterns = [
    path('', include(router.urls)),
]
