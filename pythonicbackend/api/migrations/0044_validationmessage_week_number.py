# Generated by Django 3.0.8 on 2021-01-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20210121_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='validationmessage',
            name='week_number',
            field=models.IntegerField(default=1, null=True, verbose_name='WEEKNUMBER'),
        ),
    ]