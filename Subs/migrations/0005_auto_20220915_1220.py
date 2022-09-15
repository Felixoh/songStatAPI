# Generated by Django 3.2.13 on 2022-09-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subs', '0004_remove_artistinfo_art_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistinfo',
            name='art_URI',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='art_followers',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='art_href',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='art_popularity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='art_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
