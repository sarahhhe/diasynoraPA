# Generated by Django 3.0.6 on 2020-06-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0031_campaign_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='title',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]
