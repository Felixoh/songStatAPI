# Generated by Django 3.2.13 on 2022-09-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subs', '0002_artist_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_name', models.CharField(max_length=100)),
                ('art_id', models.CharField(max_length=100)),
                ('art_followers', models.IntegerField()),
                ('art_popularity', models.IntegerField()),
                ('art_type', models.CharField(max_length=50)),
                ('art_URI', models.CharField(max_length=100)),
                ('art_href', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subs.artist')),
            ],
        ),
    ]
