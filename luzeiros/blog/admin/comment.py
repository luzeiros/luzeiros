from django.contrib import admin
from luzeiros.blog.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
