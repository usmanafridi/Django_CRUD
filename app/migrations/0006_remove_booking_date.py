# Generated by Django 3.2.8 on 2021-10-28 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
    ]
