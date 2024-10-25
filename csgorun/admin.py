from django.contrib import admin

from csgorun.models import User


@admin.register(User)
class SteamUserAdmin(admin.ModelAdmin):
    pass