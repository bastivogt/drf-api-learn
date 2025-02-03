from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name"
    ]

    list_display_links = [
        "id",
        "first_name",
        "last_name"
    ]

    search_fields = [
        "first_name",
        "last_name"
    ]





class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title"
    ]

    list_display_links = [
        "id",
        "title"
    ]

    search_fields = [
        "title"
    ]

    list_filter = [
        #"author"
    ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
