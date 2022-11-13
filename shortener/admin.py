from django.contrib import admin
from .models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Url._meta.fields]
    #list_display.insert(0, '__str__')

