from django.db import models
from .helpers.identifier import make_identifier


class Presenter(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, max_length=500)
    photo = models.ImageField(blank=True, upload_to='presenters/')
    cover_art = models.ImageField(blank=True, upload_to='presenters/')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_presenters'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
