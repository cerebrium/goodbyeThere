# Generated by Django 3.0.8 on 2021-02-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20210201_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='vehicle_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
