from django.forms import forms
from ..models.user import User


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = "__all__"
