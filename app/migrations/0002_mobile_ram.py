# Generated by Django 3.2.8 on 2021-10-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='ram',
            field=models.IntegerField(blank=True, default=4),
        ),
    ]
