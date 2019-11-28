from rest_framework import viewsets
from .router import router
from luzeiros.blog.models.comment import Comment
from luzeiros.blog.serializers.comment import CommentSerializer
from .permissions.is_author import IsAuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


router.register('comments', CommentViewSet)
