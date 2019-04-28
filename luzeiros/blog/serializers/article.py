from rest_framework import serializers
from ..models.article import Article
from ..serializers.comment import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['comments']
