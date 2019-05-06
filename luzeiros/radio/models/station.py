from django.db import models
from luzeiros.core.models.helpers.languages import LANGUAGES
from luzeiros.core.models.helpers.countries import COUNTRIES


class Station(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    frontend = models.CharField(max_length=30)
    backend = models.CharField(max_length=30)
    listen_url = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    language = models.CharField(max_length=2, default='en', choices=LANGUAGES)
    country = models.CharField(max_length=4, default='US', choices=COUNTRIES)
    artwork = models.ImageField(blank=True, upload_to='stations/artworks/')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_stations'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
