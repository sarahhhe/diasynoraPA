# Generated by Django 3.0.6 on 2020-06-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191123_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(default='ind', max_length=3),
            preserve_default=False,
        ),
    ]
