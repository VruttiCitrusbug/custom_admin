# Generated by Django 3.2.12 on 2022-05-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20220506_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewbrand',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reviewcategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]