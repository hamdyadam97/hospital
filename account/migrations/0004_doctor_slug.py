# Generated by Django 4.1 on 2022-08-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_doctor_slug_doctor_day1_of_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]
