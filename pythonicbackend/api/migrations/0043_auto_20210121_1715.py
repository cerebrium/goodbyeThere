# Generated by Django 3.0.8 on 2021-01-21 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20210120_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidationMessage',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=30, null=True)),
                ('message', models.CharField(max_length=900, null=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('station', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 21), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 1, 21), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 21), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 21), max_length=50, null=True),
        ),
    ]
