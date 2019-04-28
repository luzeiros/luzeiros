from rest_framework import routers

from .article import ArticleViewSet
from .comment import CommentViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('articles', ArticleViewSet)
router.register('comments', CommentViewSet)
