from .models import ProfileVor5
from django import forms

class FormProfileVor5(forms.ModelForm):
    class Meta:
        model = ProfileVor5
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }