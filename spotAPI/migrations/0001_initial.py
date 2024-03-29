# Generated by Django 3.2.13 on 2022-05-09 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('alb_SpotID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('alb_Name', models.CharField(max_length=255)),
                ('alb_Type', models.CharField(max_length=255)),
                ('alb_Href', models.URLField()),
                ('alb_ReleaseDate', models.DateTimeField()),
                ('alb_ReleaseDatePrecision', models.CharField(max_length=10)),
                ('alb_URI', models.URLField()),
                ('alb_total_tracks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('art_SpotID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('art_Name', models.CharField(max_length=255)),
                ('art_Popularity', models.CharField(max_length=255)),
                ('art_type', models.CharField(max_length=255)),
                ('art_URI', models.URLField()),
                ('art_followers', models.IntegerField()),
                ('alb_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.album')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('play_SpotID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('play_Name', models.CharField(max_length=255)),
                ('play_Href', models.CharField(max_length=200)),
                ('play_Descrition', models.CharField(max_length=255)),
                ('play_collabs', models.CharField(max_length=150)),
                ('play_types', models.CharField(max_length=150)),
                ('play_total_tracks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_Name', models.CharField(max_length=255)),
                ('track_SpotID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('track_No', models.IntegerField()),
                ('track_Type', models.CharField(max_length=255)),
                ('track_Popularity', models.IntegerField()),
                ('track_duration', models.BigIntegerField()),
                ('track_discNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_Height', models.IntegerField()),
                ('img_Width', models.IntegerField()),
                ('img_URI', models.URLField()),
                ('albID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.album')),
                ('artID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.artist')),
                ('playID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.playlist')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='trackID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.track'),
        ),
        migrations.AddField(
            model_name='album',
            name='trackID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spotAPI.track'),
        ),
    ]
