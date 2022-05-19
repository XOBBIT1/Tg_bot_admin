from django.contrib import admin
from .models import *
from .forms import *

@admin.register(Profile_bot2)
class AdminProfile(admin.ModelAdmin):
    list_display = ["id", "name", "data"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfile_bot2


@admin.register(Massage_bot2)
class AdminMessage(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")
    ordering = ("-id",)

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor2_bot2)
class AdminProfile2(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfileVor2_bot2

@admin.register(MassageVor2_bot2)
class AdminMessage2(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor3_bot2)
class AdminProfile3(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfileVor3_bot2

@admin.register(MassageVor3_bot2)
class AdminMessage3(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor4_bot2)
class AdminProfile4(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfileVor4_bot2

@admin.register(MassageVor4_bot2)
class AdminMessage4(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

@admin.register(ProfileVor5_bot2)
class AdminProfile5(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ("id", "name")
    ordering = ("-id",)
    form = FormProfileVor5_bot2

@admin.register(MassageVor5_bot2)
class AdminMessage5(admin.ModelAdmin):
    list_display = ["id", "name", "massege", "get_html_phot", "data", "crib"]
    fields = ("name", "massege", "image", "get_html_phot", "crib")
    readonly_fields = ("get_html_phot", "crib")

    def get_html_phot(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}'width=100>")

    get_html_phot.short_description = "Фото"

