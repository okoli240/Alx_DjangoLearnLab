from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
