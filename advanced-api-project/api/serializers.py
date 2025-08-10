from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    - Serializes all fields of the Book model (id, title, publication_year, author)
    - Adds custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        # include author id as FK value; all model fields serialized
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the book's publication year is not in the future.
        This validator is run automatically when DRF validates the serializer.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    - Serializes the Author.name field
    - Includes a nested list of books related to the author.
      The nested books are serialized with BookSerializer.
    How relationship is handled:
    - In the Book model we set `author = ForeignKey(..., related_name='books')`.
      That allows us to reference the related set via `author_instance.books`.
    - Here we use BookSerializer(many=True, read_only=True) to embed
      the related books inside the Author representation.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
