# Generated by Django 4.1.4 on 2023-01-23 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBookPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_books/files/covers')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_books.photobook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
