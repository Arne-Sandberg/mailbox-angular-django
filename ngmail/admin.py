from django.contrib import admin
from ngmail.models import NGUser, NGMessage


class NGUserAdmin(admin.ModelAdmin):
    pass


class NGMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(NGUser, NGUserAdmin)
admin.site.register(NGMessage, NGMessageAdmin)