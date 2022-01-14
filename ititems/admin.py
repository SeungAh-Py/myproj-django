from django.contrib import admin
from ititems.models import Ititems


@admin.register(Ititems)
class ItitemsAdmin(admin.ModelAdmin):
    list_display = ["name", "company"]
    list_display_links = ["name"]
    search_fields = ["name"]
