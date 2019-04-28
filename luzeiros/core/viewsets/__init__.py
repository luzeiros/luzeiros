from rest_framework import routers
from .user import UserViewSet


router = routers.SimpleRouter(trailing_slash=False)

router.register('users', UserViewSet)
