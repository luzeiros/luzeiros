from django.contrib import admin
from luzeiros.blog.models.comment import Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
