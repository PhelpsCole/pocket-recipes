# Generated by Django 3.2.13 on 2022-07-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220716_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='count',
        ),
    ]
