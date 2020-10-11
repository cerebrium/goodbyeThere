# Generated by Django 3.0.8 on 2020-10-11 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20201002_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleddate',
            name='week_number',
            field=models.CharField(max_length=30, null=True, verbose_name='weekNumber'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50),
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.CharField(default='16:43:26', max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='logIn_time',
            field=models.IntegerField(default=1, null=True, verbose_name='WEEKNUMBER'),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
    ]
