# Generated by Django 4.1 on 2022-08-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_doctor_is_active_remove_doctor_num_verify_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isactive',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
