from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from luzeiros.core.models.user import User
from luzeiros.blog.admin.inlines.article import ArticleInline
from luzeiros.blog.admin.inlines.comment import CommentInline


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [ArticleInline, CommentInline]
    list_display = ['id', 'name', 'auth_token', 'is_verified', 'is_app']
    list_editable = ['is_app']
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    readonly_fields = ('date_joined', 'last_login',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'photo', 'is_app'),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')

    # Ensure applications cannot write in admin site
    def has_add_permission(self, request):
        return not request.user.is_app or not request.user.is_active

    def has_change_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active
