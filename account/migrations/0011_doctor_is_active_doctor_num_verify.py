# Generated by Django 4.1 on 2022-08-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_doctor_day1_of_work_alter_doctor_day2_of_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='num_verify',
            field=models.IntegerField(blank=True, null=True, verbose_name='num_verify'),
        ),
    ]
