# Generated by Django 4.1.7 on 2023-03-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_notes_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='url',
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
    ]
