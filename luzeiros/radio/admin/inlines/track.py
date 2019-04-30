from django.contrib import admin
from luzeiros.radio.models.track import Track


class TrackInline(admin.StackedInline):
    model = Track
    extra = 1
