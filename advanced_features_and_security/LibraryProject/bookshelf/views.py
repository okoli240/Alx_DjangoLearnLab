from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # your form logic here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # your update logic here
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # your delete logic here
    pass
"""
## Permissions and Groups Setup

- Defined custom model permissions in `CustomUser`:
  - can_view, can_create, can_edit, can_delete
- Created groups via Django Admin:
  - Viewers: can_view
  - Editors: can_view, can_create, can_edit
  - Admins: all permissions
- Used `@permission_required` to restrict view access to only users with specific permissions.
- Assign users to groups using Django Admin.
- Permissions are enforced in views using decorators like:
  @permission_required('bookshelf.can_edit', raise_exception=True)
"""