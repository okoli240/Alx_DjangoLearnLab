from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books (read-only access for everyone)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view

# DetailView: Retrieve a single book by ID (read-only access for everyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView: Add a new book (only authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView: Modify an existing book (only authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.request.data.get('id') or self.request.query_params.get('id')
        if not pk:
            raise NotFound("Missing 'id' in request data or query parameters.")
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")

# DeleteView: Remove a book (only authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.request.data.get('id') or self.request.query_params.get('id')
        if not pk:
            raise NotFound("Missing 'id' in request data or query parameters.")
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")
