# Generated by Django 3.0.8 on 2021-05-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20210510_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='vtype',
            field=models.CharField(default='Standard', max_length=20, null=True),
        ),
    ]