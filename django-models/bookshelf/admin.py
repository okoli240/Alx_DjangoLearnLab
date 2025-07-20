from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # shows these columns in admin list
    list_filter = ('publication_year', 'author')            # adds filters on the sidebar
    search_fields = ('title', 'author')                     # enables search box
