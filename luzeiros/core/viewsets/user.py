from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .router import router
from luzeiros.core.models.user import User
from luzeiros.core.serializers.user import UserSerializer
from .permissions.is_user import IsUserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ['id', 'username', 'first_name', 'last_name', 'email']
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    filterset_fields = {
        'id': ('in', 'exact', 'lt', 'gt', 'gte', 'lte'),
        'username': ('contains', 'icontains', 'iexact'),
        'first_name': ('contains', 'icontains', 'iexact'),
        'last_name': ('contains', 'icontains', 'iexact'),
        'email': ('contains', 'icontains', 'iexact'),
    }

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        queryset = User.objects.get(username=request.user)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)


router.register('users', UserViewSet)
