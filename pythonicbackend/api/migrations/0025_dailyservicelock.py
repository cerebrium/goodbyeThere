# Generated by Django 3.0.8 on 2020-11-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20201112_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyServiceLock',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
