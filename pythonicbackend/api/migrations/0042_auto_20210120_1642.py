# Generated by Django 3.0.8 on 2021-01-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20210120_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
