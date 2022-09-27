# Generated by Django 3.2.12 on 2022-08-09 07:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_reviewframeset_suspension_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('comment_type', models.CharField(choices=[('Review', 'Review'), ('Brand', 'Brand'), ('Category', 'Category'), ('Custom_Landing', 'Custom Landing')], default='Review', max_length=255)),
                ('comment_type_id', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.comments')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comments',
            },
        ),
        migrations.AddIndex(
            model_name='comments',
            index=models.Index(fields=['id'], name='comments_id_758ccd_idx'),
        ),
        migrations.AddIndex(
            model_name='comments',
            index=models.Index(fields=['ip', 'is_approved'], name='comments_ip_552c1b_idx'),
        ),
    ]
