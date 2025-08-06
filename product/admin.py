from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_bio')
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20

    def short_bio(self, obj):
        return (obj.bio[:75] + '...') if obj.bio and len(obj.bio) > 75 else obj.bio
    short_bio.short_description = "Bio Preview"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'author', 'publication_year', 'price', 'status', 'pages', 'created_at', 'updated_at'
    )
    list_filter = ('status', 'author', 'publication_year')
    search_fields = ('name', 'author__name')
    ordering = ('-created_at',)
    date_hierarchy = 'publication_year'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Book Info", {
            "fields": ("name", "author", "publication_year", "pages", "price", "status")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
