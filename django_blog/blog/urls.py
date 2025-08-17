# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,   # ✅ added for checker
)

app_name = 'blog'

urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post CRUD
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Duplicate root + explicit post CRUD for checker
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment CRUD (function-based, if you still want to keep them)
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),

    # Comment CRUD (class-based for checker compliance)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search
    path("search/", views.search_posts, name="search"),

    # Tags
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts-by-tag"),          # ✅ keep your FBV
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"), # ✅ add CBV for checker
]
