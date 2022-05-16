from .models import Profile_bot5
from django import forms

class FormProfile_bot5(forms.ModelForm):
    class Meta:
        model = Profile_bot5
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }