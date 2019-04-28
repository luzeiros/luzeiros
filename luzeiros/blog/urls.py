from django.urls import path, include
from .viewsets import router


urlpatterns = [
    path('', include(router.urls)),
]
