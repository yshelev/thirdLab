from django.contrib import admin

from csgorun.models import User, SiteUser


admin.site.register(SiteUser)

@admin.register(User)
class SteamUserAdmin(admin.ModelAdmin):
    pass