from .models import ProfileVor3
from django import forms

class FormProfileVor3(forms.ModelForm):
    class Meta:
        model = ProfileVor3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }