# Generated by Django 3.0.8 on 2021-04-21 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_auto_20210419_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='validationsheet',
            name='Jumper',
            field=models.IntegerField(default=0, null=True, verbose_name='Jumper'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 4, 21), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 4, 21), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 4, 21), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='DpmoBonus',
            field=models.IntegerField(default=0, null=True, verbose_name='dpmo bonus'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='Missortfourth',
            field=models.IntegerField(default=0, null=True, verbose_name='missort fourth'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='Missortsixth',
            field=models.IntegerField(default=0, null=True, verbose_name='missort sixth'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R2',
            field=models.IntegerField(default=0, null=True, verbose_name='r2'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R4',
            field=models.IntegerField(default=0, null=True, verbose_name='r4'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R6',
            field=models.IntegerField(default=0, null=True, verbose_name='r6'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalLVP',
            field=models.IntegerField(default=0, null=True, verbose_name='total large vehicle payment'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalLwp',
            field=models.IntegerField(default=0, null=True, verbose_name='total late wave payment'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalTraining',
            field=models.IntegerField(default=0, null=True, verbose_name='training'),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 4, 21), max_length=50, null=True),
        ),
    ]
