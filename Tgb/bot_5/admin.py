from django.contrib import admin
from .models import *
from .forms import *

@admin.register(Profile_bot5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "data"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot5


@admin.register(Massage_bot5)
class AdminMessage(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor2_bot5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot5

@admin.register(MassageVor2_bot5)
class AdminMessage2(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor3_bot5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot5

@admin.register(MassageVor3_bot5)
class AdminMessage3(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor4_bot5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot5

@admin.register(MassageVor4_bot5)
class AdminMessage4(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor5_bot5)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot5

@admin.register(MassageVor5_bot5)
class AdminMessage5(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"