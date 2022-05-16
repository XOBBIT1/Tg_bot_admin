from django.contrib import admin
from .models import ProfileVor2, MassageVor2
from .forms import FormProfileVor2


@admin.register(MassageVor2)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "image", "data"]
    ordering = ("-id",)
