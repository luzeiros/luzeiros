from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from luzeiros.blog.models.article import Article
from luzeiros.blog.models.comment import Comment
from luzeiros.core.models.user import User
from luzeiros.blog.serializers.article import ArticleSerializer
from luzeiros.blog.serializers.comment import CommentSerializer
from luzeiros.core.serializers.user import UserSerializer
from .permissions.is_author import IsAuthorOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.exclude(is_private=True)
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_private:
            serializer = self.get_serializer(self.get_object())
            return Response(serializer.data)
        return Response([])

    @action(detail=True)
    def author(self, request, pk=None):
        user = User.objects.get(id=self.get_object().author_id)
        self.serializer_class = UserSerializer
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=True)
    def comments(self, request, pk=None):
        comments = Comment.objects.filter(article=self.get_object())
        self.serializer_class = CommentSerializer

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def liked(self, request):
        articles = self.queryset.filter(likes__username=request.user)

        page = self.paginate_queryset(articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)
