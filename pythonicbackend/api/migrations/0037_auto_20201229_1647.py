# Generated by Django 3.0.8 on 2020-12-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20201229_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validationsheet',
            name='DpmoBonus',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='Missortfourth',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='Missortsixth',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R2',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R4',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='R6',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='miles',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalLVP',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalLwp',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
        migrations.AlterField(
            model_name='validationsheet',
            name='totalTraining',
            field=models.IntegerField(default=0, null=True, verbose_name='miles'),
        ),
    ]
