from django import forms
from .models import E_mart


class E_martForm(forms.ModelForm):
    class Meta:
        model = E_mart
        fields = "__all__"
