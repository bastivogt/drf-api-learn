from django.contrib import admin

from .models import Person



class PersonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "birthday",
        "gender"
    ]

    list_display_links = [
        "id",
        "first_name",
        "last_name"
    ]

    list_editable = [
        "gender"
    ]

    list_filter = [
        "gender"
    ]

    search_fields = [
        "first_name",
        "last_name"
    ]

admin.site.register(Person, PersonAdmin)
