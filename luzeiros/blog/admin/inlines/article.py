from django.contrib import admin
from luzeiros.blog.models.article import Article


class ArticleInline(admin.StackedInline):
    model = Article
    extra = 1
