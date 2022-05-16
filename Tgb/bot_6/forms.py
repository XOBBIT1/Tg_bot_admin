from .models import Profile_bot6
from django import forms

class FormProfile_bot6(forms.ModelForm):
    class Meta:
        model = Profile_bot6
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }