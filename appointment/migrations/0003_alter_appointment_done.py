# Generated by Django 4.1 on 2022-08-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_rate_notes_alter_appointment_date_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='done',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
