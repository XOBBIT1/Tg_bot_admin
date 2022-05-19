from .models import *
from django import forms

class FormProfile_bot4(forms.ModelForm):
    class Meta:
        model = Profile_bot3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor2_bot4(forms.ModelForm):
    class Meta:
        model = ProfileVor2_bot3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor3_bot4(forms.ModelForm):
    class Meta:
        model = ProfileVor3_bot3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor4_bot4(forms.ModelForm):
    class Meta:
        model = ProfileVor4_bot3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor5_bot4(forms.ModelForm):
    class Meta:
        model = ProfileVor5_bot3
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }
