# Generated by Django 3.0.8 on 2021-05-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_auto_20210511_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliancevan',
            name='next',
            field=models.CharField(max_length=30, null=True),
        ),
    ]