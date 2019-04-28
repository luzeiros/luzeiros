from django.contrib import admin
from luzeiros.blog.models.article import Article
from luzeiros.blog.admin.inlines.comment import CommentInline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'slug', 'comments_count', 'likes_count', 'updated_at']
    list_editable = ['is_private']
    inlines = [CommentInline]
    readonly_fields = ['author']
    prepopulated_fields = {'slug': ('title',)}

    # Ensure applications cannot write in admin site
    def has_add_permission(self, request):
        return not request.user.is_app or not request.user.is_active

    def has_change_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    # Ensure current user is assigned as author of article
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author_id = request.user.id
        obj.save()
