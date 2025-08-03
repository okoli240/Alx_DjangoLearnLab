from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import BookList 
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
# Set up the DRF router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- Token endpoint
    # All CRUD operations handled by router
    path('', include(router.urls)),
]

