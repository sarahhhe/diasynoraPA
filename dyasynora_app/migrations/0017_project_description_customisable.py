# Generated by Django 3.0.6 on 2020-06-04 20:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0016_auto_20200602_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_customisable',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
