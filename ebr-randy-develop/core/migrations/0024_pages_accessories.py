# Generated by Django 3.2.12 on 2022-05-04 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20220503_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='accessories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
