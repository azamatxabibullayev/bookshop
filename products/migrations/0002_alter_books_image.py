# Generated by Django 5.0.6 on 2024-05-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(default='default_img/default_book_img.png', upload_to='books/'),
        ),
    ]