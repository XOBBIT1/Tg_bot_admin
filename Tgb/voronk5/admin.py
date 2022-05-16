from django.contrib import admin
from .models import  MassageVor5


@admin.register(MassageVor5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "image", "data"]
    ordering = ("-id",)
