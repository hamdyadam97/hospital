# Generated by Django 4.1 on 2022-08-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_doctor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='day1_of_work',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='day1_of_work'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='day2_of_work',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='day2_of_work'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='day3_of_work',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='day3_of_work'),
        ),
    ]
