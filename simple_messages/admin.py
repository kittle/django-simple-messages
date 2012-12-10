from django.contrib import admin

from models import SimpleMessage


class SimpleMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(SimpleMessage, SimpleMessageAdmin)
