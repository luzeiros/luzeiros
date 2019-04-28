from rest_framework import serializers
from luzeiros.radio.models.program import Program


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = "__all__"
