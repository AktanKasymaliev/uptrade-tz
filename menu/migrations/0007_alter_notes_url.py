# Generated by Django 4.1.7 on 2023-03-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_notes_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='url',
            field=models.SlugField(max_length=300, unique=True),
        ),
    ]
