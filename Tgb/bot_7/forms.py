from .models import Profile_bot7
from django import forms

class FormProfile_bot7(forms.ModelForm):
    class Meta:
        model = Profile_bot7
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }