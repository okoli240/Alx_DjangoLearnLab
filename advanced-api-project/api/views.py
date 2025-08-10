from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.

    Filtering allowed on: title, author__name, publication_year
    Searching allowed on: title, author__name
    Ordering allowed on: title, publication_year, author__name
    """
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.request.data.get('id') or self.request.query_params.get('id')
        if not pk:
            raise NotFound("Missing 'id' in request data or query parameters.")
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.request.data.get('id') or self.request.query_params.get('id')
        if not pk:
            raise NotFound("Missing 'id' in request data or query parameters.")
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")
