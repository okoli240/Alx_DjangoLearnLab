# Delete Book Instance

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
# <QuerySet []>
