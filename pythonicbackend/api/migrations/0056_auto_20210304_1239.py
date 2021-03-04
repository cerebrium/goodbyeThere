# Generated by Django 3.0.8 on 2021-03-04 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_auto_20210302_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackerclass',
            name='latitude',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='trackerclass',
            name='longitude',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 4), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 3, 4), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 4), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 4), max_length=50, null=True),
        ),
    ]
