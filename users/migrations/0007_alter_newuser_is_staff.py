# Generated by Django 3.2.13 on 2022-09-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usersettings_verification_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]