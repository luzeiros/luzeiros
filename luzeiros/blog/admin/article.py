from django.contrib import admin
from luzeiros.blog.models.article import Article
from luzeiros.blog.admin.inlines.comment import CommentInline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
