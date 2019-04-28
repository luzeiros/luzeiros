from django.db import models
from .helpers.identifier import make_identifier
from luzeiros.core.models.user import User
from luzeiros.blog.models.article import Article


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.DO_NOTHING)
    content = models.TextField(blank=True)
    flagged = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'blog_comments'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def username(self):
        return self.author.username

    @property
    def author_status(self):
        return self.author.is_verified

    def __str__(self):
        return f'#{self.id} {self.article.title}'
