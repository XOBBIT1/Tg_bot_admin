from .models import ProfileVor2
from django import forms

class FormProfileVor2(forms.ModelForm):
    class Meta:
        model = ProfileVor2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }