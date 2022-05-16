from .models import Profile_bot2
from django import forms

class FormProfile_bot2(forms.ModelForm):
    class Meta:
        model = Profile_bot2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }