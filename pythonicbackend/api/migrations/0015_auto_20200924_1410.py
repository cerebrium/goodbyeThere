# Generated by Django 3.0.8 on 2020-09-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200924_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.CharField(default='14:10:23', max_length=50),
        ),
    ]
