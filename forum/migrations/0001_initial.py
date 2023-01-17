# Generated by Django 4.1.4 on 2022-12-24 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('full_text', models.TextField(verbose_name='Review')),
                ('date', models.DateField(verbose_name='Date of publication')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Site Forum',
            },
        ),
        migrations.CreateModel(
            name='ForumComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField(blank=True, verbose_name='FullText')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
