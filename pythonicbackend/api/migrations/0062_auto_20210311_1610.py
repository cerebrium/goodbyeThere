# Generated by Django 3.0.8 on 2021-03-11 16:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_auto_20210311_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleddate',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='manager_movement',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), blank=True, default=list, size=None),
        ),
    ]
