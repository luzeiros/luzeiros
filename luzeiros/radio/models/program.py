from django.db import models
from recurrence.fields import RecurrenceField
from .helpers.identifier import make_identifier
from .presenter import Presenter


class Program(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(blank=True, max_length=30)
    presenter = models.ForeignKey(Presenter, related_name='programs', on_delete=models.DO_NOTHING)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    artwork = models.ImageField(blank=True, upload_to='uploads/')
    featured = models.BooleanField(default=False)
    recurrences = RecurrenceField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'radio_programs'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
