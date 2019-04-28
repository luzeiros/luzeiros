from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from rest_framework.authtoken.models import Token
from .helpers.identifier import make_identifier
from .helpers.languages import LANGUAGES


class User(AbstractUser):
    id = models.BigIntegerField(primary_key=True, editable=False)
    is_verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='users/photos/', blank=True)
    is_app = models.BooleanField(default=False)
    languages = ArrayField(
        models.CharField(max_length=3, choices=LANGUAGES, default=['pt']), null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'core_users'
        ordering = ['-created_at']

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()
        self.username = self.username.lower()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user_id=self.id)
    
    def __str__(self):
        return self.username
