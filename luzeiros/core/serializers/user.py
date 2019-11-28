from rest_framework import serializers
from luzeiros.core.models.user import User
from luzeiros.blog.serializers.article import ArticleSerializer
from luzeiros.blog.serializers.comment import CommentSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'password',
            'is_active',
            'is_superuser',
            'is_staff',
            'is_app',
            'last_login',
            'date_joined',
            'user_permissions',
            'email',
            'groups',
        )
