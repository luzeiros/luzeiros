from rest_framework import viewsets
from rest_framework import permissions
from luzeiros.radio.models.program import Program
from luzeiros.radio.serializers.program import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
