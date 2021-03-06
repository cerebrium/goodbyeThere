# Generated by Django 3.0.8 on 2021-03-25 16:48

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_dailymessage_datesubmit'),
    ]

    operations = [
        migrations.CreateModel(
            name='EightHourList',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerChangeList',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100, null=True)),
                ('week_number', models.CharField(max_length=10, null=True)),
                ('station', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 3, 25), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 25), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 3, 25), max_length=50, null=True),
        ),
    ]
