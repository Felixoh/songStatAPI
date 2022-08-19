# Generated by Django 3.2.13 on 2022-08-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220817_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Advanced', 'Advance'), ('Extended', 'Extended'), ('Premium', 'Premium'), ('Free', 'Free'), ('Medium', 'Medium')], default='Free', max_length=30),
        ),
    ]
