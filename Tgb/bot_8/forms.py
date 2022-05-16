from .models import Profile_bot8
from django import forms

class FormProfile_bot8(forms.ModelForm):
    class Meta:
        model = Profile_bot8
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }