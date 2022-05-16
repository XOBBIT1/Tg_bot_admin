from .models import Profile_bot4
from django import forms

class FormProfile_bot4(forms.ModelForm):
    class Meta:
        model = Profile_bot4
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }