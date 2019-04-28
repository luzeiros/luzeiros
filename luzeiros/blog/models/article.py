from django.db import models
from django.contrib.postgres.fields import ArrayField
from .helpers.identifier import make_identifier
from luzeiros.core.models.helpers.languages import LANGUAGES
from luzeiros.core.models.user import User


class Article(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(User, related_name='articles', on_delete=models.DO_NOTHING)
    title = models.CharField(blank=True, max_length=30)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='uploads')
    language = models.CharField(max_length=3, choices=LANGUAGES, default='pt')
    is_private = models.BooleanField(default=False)

    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    tags = ArrayField(
        models.CharField(max_length=10), blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'blog_articles'
        ordering = ['-created_at']

    @property
    def author_name(self):
        return self.author.name

    @property
    def comments_count(self):
        return self.comments.count()

    @property
    def likes_count(self):
        return self.likes.count()
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
