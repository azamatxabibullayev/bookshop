from django.contrib import admin
from .models import Book, CategoryBook, BookAuthor, LanguageBook, Review, Author
# Register your models here.

admin.site.register(Book)
admin.site.register(CategoryBook)
admin.site.register(BookAuthor)
admin.site.register(LanguageBook)
admin.site.register(Review)
admin.site.register(Author)
