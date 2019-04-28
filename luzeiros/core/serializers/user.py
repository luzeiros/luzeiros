from rest_framework import serializers
from luzeiros.core.models.user import User
from luzeiros.blog.serializers.article import ArticleSerializer
from luzeiros.blog.serializers.comment import CommentSerializer


class UserSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, allow_null=True)

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login', 'user_permissions')

    class JSONAPIMeta:
        included_resources = ['articles', 'comments']

    def get_articles(self, obj):
        return obj.articles.exclude(is_private=True)
