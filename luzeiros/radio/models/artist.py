from django.db import models
from .helpers.identifier import make_identifier
from .helpers.music import path_for_artist


class Artist(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, upload_to=path_for_artist)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_artists'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def albums_count(self):
        return self.albums.count()

    def __str__(self):
        return self.name
