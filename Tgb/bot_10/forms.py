from .models import Profile_bot10
from django import forms

class FormProfile_bot10(forms.ModelForm):
    class Meta:
        model = Profile_bot10
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }