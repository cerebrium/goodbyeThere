# Generated by Django 3.0.8 on 2020-08-19 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200810_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='registration',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='vtype',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 19), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 8, 19), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 19), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 19), max_length=50, null=True),
        ),
    ]