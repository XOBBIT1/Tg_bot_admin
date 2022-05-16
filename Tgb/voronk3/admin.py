from django.contrib import admin
from .models import ProfileVor3, MassageVor3
from .forms import FormProfileVor3


@admin.register(MassageVor3)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "image", "data"]
    ordering = ("-id",)
