from .models import ProfileVor4
from django import forms

class FormProfileVor4(forms.ModelForm):
    class Meta:
        model = ProfileVor4
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }