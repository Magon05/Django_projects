from django import forms
from .models import Otdelenia


class Editform(forms.ModelForm):

    class Meta:

        model = Otdelenia
        fields = "__all__"
