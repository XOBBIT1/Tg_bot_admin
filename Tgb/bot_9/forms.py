from .models import Profile_bot9
from django import forms

class FormProfile_bot9(forms.ModelForm):
    class Meta:
        model = Profile_bot9
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }