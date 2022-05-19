from .models import *
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

class FormProfileVor2_bot2(forms.ModelForm):
    class Meta:
        model = ProfileVor2_bot2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor3_bot2(forms.ModelForm):
    class Meta:
        model = ProfileVor3_bot2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor4_bot2(forms.ModelForm):
    class Meta:
        model = ProfileVor4_bot2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }

class FormProfileVor5_bot2(forms.ModelForm):
    class Meta:
        model = ProfileVor5_bot2
        fields = {
            "id",
            "name",
        }
        widgets = {
            "name": forms.TextInput
        }