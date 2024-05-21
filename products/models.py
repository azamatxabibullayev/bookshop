from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class CategoryBook(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'category_book'

    def __str__(self):
        return self.name
    
class LanguageBook(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'language_book'

    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='books/',default='default_images/book_image.png', blank=True,null=True)
    category=models.ForeignKey(CategoryBook,on_delete=models.CASCADE)
    page=models.IntegerField() 
    book_lang=models.ForeignKey(LanguageBook, on_delete=models.DO_NOTHING)

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class BookAuthor(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f'{self.book.title} by {self.author.first_name} {self.author.last_name}'
    
class Review(models.Model):
    comment=models.CharField(max_length=100)
    rating=models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.rating} - {self.book.title} review by {self.user.username}'


