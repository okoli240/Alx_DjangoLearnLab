# Django Admin Configuration for Book Model

## Registration
The Book model was registered in `bookshelf/admin.py` using the `@admin.register(Book)` decorator.

## Custom Admin Configuration

The following customizations were added:

- `list_display = ('title', 'author', 'publication_year')`  
  ➤ Displays key fields in the list view.

- `list_filter = ('publication_year', 'author')`  
  ➤ Enables sidebar filters to refine book entries.

- `search_fields = ('title', 'author')`  
  ➤ Adds a search box to quickly find books by title or author.

These changes improve usability and visibility of book records in the Django admin interface.
