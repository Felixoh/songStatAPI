# Generated by Django 3.2.13 on 2022-09-14 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_usersettings_verification_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='verification_expires',
            field=models.DateField(default=datetime.date(2022, 9, 17)),
        ),
    ]
