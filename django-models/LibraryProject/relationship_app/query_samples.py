from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author):
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def librarian_for_library(library):
    return Librarian.objects.get(library=library)
