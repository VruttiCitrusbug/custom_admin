# Generated by Django 3.2.12 on 2022-05-25 08:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20220524_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='more_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
