from django.contrib import admin
from .models import *
from .forms import FormProfile

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "data"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile


@admin.register(Massage)
class AdminMessage(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data"]
    fields = ( "name", "massege", "image", "get_html_phot")
    readonly_fields = ("get_html_phot",)
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(MassageVor2)
class AdminMessage2(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data"]
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(MassageVor3)
class AdminMessage3(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data"]
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(MassageVor4)
class AdminMessage4(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data"]
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(MassageVor5)
class AdminMessage5(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data"]
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

