# Generated by Django 4.1.4 on 2023-03-24 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='cat_catrgory',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='cat_user',
        ),
        migrations.DeleteModel(
            name='CategoryQuestions',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]