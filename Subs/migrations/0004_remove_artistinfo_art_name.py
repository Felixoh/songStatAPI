# Generated by Django 3.2.13 on 2022-09-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subs', '0003_artistinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistinfo',
            name='art_name',
        ),
    ]
