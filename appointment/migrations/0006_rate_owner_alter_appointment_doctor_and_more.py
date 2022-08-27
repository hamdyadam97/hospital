# Generated by Django 4.1 on 2022-08-20 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_doctor_day1_of_work_alter_doctor_day2_of_work_and_more'),
        ('patient', '0003_alter_patient_user'),
        ('appointment', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='owner',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to='account.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app', to='appointment.appointment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='read',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]