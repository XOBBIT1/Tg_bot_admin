from django.contrib import admin
from .models import ProfileVor4, MassageVor4
from .forms import FormProfileVor4


@admin.register(MassageVor4)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "image", "data"]
    ordering = ("-id",)
