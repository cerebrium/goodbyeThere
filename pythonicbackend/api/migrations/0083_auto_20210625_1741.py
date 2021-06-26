# Generated by Django 3.0.8 on 2021-06-25 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_auto_20210617_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='validationmessage',
            name='foreignKey',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 6, 25), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 6, 25), max_length=50, null=True),
        ),
    ]
