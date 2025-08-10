from django.db import models

class Author(models.Model):
    """
    Author model
    - name: the author's full name (string)
    Purpose: Represents an author who can have multiple Book instances.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model
    - title: the title of the book (string)
    - publication_year: integer year the book was published
    - author: ForeignKey to Author establishing a one-to-many (Author -> Books)
    Purpose: Represents a published book and links it to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # related_name 'books' allows author_instance.books.all() and helps nested serialization
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
