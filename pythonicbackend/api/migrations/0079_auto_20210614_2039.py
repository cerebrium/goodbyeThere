# Generated by Django 3.0.8 on 2021-06-14 20:39

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0078_auto_20210610_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='startList',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 14), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 6, 14), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 14), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 14), max_length=50, null=True),
        ),
    ]
