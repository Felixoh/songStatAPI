# Generated by Django 3.2.13 on 2022-08-17 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220815_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user_membership',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='users.usermembership'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='verification_expires',
            field=models.DateField(default=datetime.date(2022, 8, 20)),
        ),
    ]
