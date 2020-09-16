# Generated by Django 3.0.8 on 2020-08-25 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_driver_compliancecheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleddate',
            name='totalRouteForDay',
            field=models.CharField(default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 8, 25), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 25), max_length=50, null=True),
        ),
    ]