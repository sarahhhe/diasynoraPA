# Generated by Django 3.0.6 on 2020-06-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0022_auto_20200606_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='%d/%m/%Y %H:%M:%S'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='%d/%m/%Y %H:%M:%S'),
        ),
    ]
