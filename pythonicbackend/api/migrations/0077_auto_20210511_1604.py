# Generated by Django 3.0.8 on 2021-05-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_auto_20210511_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliancevan',
            name='next',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
