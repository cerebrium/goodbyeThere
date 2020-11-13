# Generated by Django 3.0.8 on 2020-11-12 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20201107_1748'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.AddField(
            model_name='dailymessage',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='dailymessage',
            name='message',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 12), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 11, 12), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 12), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 12), max_length=50, null=True),
        ),
    ]
