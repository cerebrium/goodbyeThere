# Generated by Django 3.0.8 on 2020-08-25 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200825_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleddate',
            name='driver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Driver'),
        ),
    ]