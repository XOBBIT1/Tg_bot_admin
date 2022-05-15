from .models import Profile
from django import forms

class FormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }