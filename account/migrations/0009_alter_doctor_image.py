# Generated by Django 4.1 on 2022-08-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_doctor_avg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, default='E:/GP/media/profile/l.jpg', null=True, upload_to='profile', verbose_name=' image'),
        ),
    ]