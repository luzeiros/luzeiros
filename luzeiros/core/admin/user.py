from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from luzeiros.core.models.user import User
from luzeiros.blog.admin.inlines.article import ArticleInline
from luzeiros.blog.admin.inlines.comment import CommentInline


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [ArticleInline, CommentInline]
    list_display = ['first_name', 'last_name', 'is_verified']
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    readonly_fields = ('date_joined', 'last_login',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'photo'),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
