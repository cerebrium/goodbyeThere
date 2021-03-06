# Generated by Django 3.0.8 on 2021-03-11 14:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_auto_20210311_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleddate',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='validationsheet',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='vehiclescheduleddate',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
    ]
