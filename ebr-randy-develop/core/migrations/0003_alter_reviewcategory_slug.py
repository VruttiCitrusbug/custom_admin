# Generated by Django 3.2.12 on 2022-03-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220324_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
