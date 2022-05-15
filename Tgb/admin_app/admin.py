from django.contrib import admin
from .models import Profile, Massage
from .forms import FormProfile

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ("-id",)
    form = FormProfile

@admin.register(Massage)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "image", "data"]
    ordering = ("-id",)
