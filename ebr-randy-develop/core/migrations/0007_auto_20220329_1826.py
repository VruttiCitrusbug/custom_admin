# Generated by Django 3.2.12 on 2022-03-29 12:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220329_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='additional_motors',
        ),
        migrations.RemoveField(
            model_name='review',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='review',
            name='battery_watt_hours',
        ),
        migrations.RemoveField(
            model_name='review',
            name='belt_drive',
        ),
        migrations.RemoveField(
            model_name='review',
            name='bike_class',
        ),
        migrations.RemoveField(
            model_name='review',
            name='brake_type',
        ),
        migrations.RemoveField(
            model_name='review',
            name='cassette',
        ),
        migrations.RemoveField(
            model_name='review',
            name='chainring',
        ),
        migrations.RemoveField(
            model_name='review',
            name='charger',
        ),
        migrations.RemoveField(
            model_name='review',
            name='crankset',
        ),
        migrations.RemoveField(
            model_name='review',
            name='cvt',
        ),
        migrations.RemoveField(
            model_name='review',
            name='display',
        ),
        migrations.RemoveField(
            model_name='review',
            name='electronic_shifting',
        ),
        migrations.RemoveField(
            model_name='review',
            name='fenders',
        ),
        migrations.RemoveField(
            model_name='review',
            name='fork',
        ),
        migrations.RemoveField(
            model_name='review',
            name='frame',
        ),
        migrations.RemoveField(
            model_name='review',
            name='frame_type',
        ),
        migrations.RemoveField(
            model_name='review',
            name='front_brake',
        ),
        migrations.RemoveField(
            model_name='review',
            name='front_derailleur',
        ),
        migrations.RemoveField(
            model_name='review',
            name='front_hub',
        ),
        migrations.RemoveField(
            model_name='review',
            name='front_rack',
        ),
        migrations.RemoveField(
            model_name='review',
            name='front_wheel',
        ),
        migrations.RemoveField(
            model_name='review',
            name='gears',
        ),
        migrations.RemoveField(
            model_name='review',
            name='grips',
        ),
        migrations.RemoveField(
            model_name='review',
            name='handlebar',
        ),
        migrations.RemoveField(
            model_name='review',
            name='headlight',
        ),
        migrations.RemoveField(
            model_name='review',
            name='headset',
        ),
        migrations.RemoveField(
            model_name='review',
            name='igh',
        ),
        migrations.RemoveField(
            model_name='review',
            name='load_capacity',
        ),
        migrations.RemoveField(
            model_name='review',
            name='motor',
        ),
        migrations.RemoveField(
            model_name='review',
            name='motor_nominal_output',
        ),
        migrations.RemoveField(
            model_name='review',
            name='motor_type',
        ),
        migrations.RemoveField(
            model_name='review',
            name='pedals',
        ),
        migrations.RemoveField(
            model_name='review',
            name='price',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_brake',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_derailleur',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_hub',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_rack',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_shock',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rear_wheel',
        ),
        migrations.RemoveField(
            model_name='review',
            name='saddle',
        ),
        migrations.RemoveField(
            model_name='review',
            name='seatpost',
        ),
        migrations.RemoveField(
            model_name='review',
            name='seatpost_diameter',
        ),
        migrations.RemoveField(
            model_name='review',
            name='shift_levers',
        ),
        migrations.RemoveField(
            model_name='review',
            name='smart_bike',
        ),
        migrations.RemoveField(
            model_name='review',
            name='stem',
        ),
        migrations.RemoveField(
            model_name='review',
            name='suspension',
        ),
        migrations.RemoveField(
            model_name='review',
            name='taillight',
        ),
        migrations.RemoveField(
            model_name='review',
            name='theft_gps',
        ),
        migrations.RemoveField(
            model_name='review',
            name='tires',
        ),
        migrations.RemoveField(
            model_name='review',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='review',
            name='wheel_size',
        ),
        migrations.CreateModel(
            name='ReviewSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('bike_class', models.CharField(blank=True, max_length=200, null=True)),
                ('frame_type', models.CharField(blank=True, max_length=200, null=True)),
                ('frame', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
                ('load_capacity', models.CharField(blank=True, max_length=200, null=True)),
                ('suspension', models.CharField(blank=True, max_length=200, null=True)),
                ('fork', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_shock', models.CharField(blank=True, max_length=200, null=True)),
                ('wheel_size', models.CharField(blank=True, max_length=200, null=True)),
                ('front_wheel', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_wheel', models.CharField(blank=True, max_length=200, null=True)),
                ('front_hub', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_hub', models.CharField(blank=True, max_length=200, null=True)),
                ('tires', models.CharField(blank=True, max_length=200, null=True)),
                ('gears', models.CharField(blank=True, max_length=200, null=True)),
                ('shift_levers', models.CharField(blank=True, max_length=200, null=True)),
                ('front_derailleur', models.CharField(blank=True, max_length=200, null=True)),
                ('crankset', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_derailleur', models.CharField(blank=True, max_length=200, null=True)),
                ('electronic_shifting', models.CharField(blank=True, max_length=200, null=True)),
                ('igh', models.CharField(blank=True, max_length=200, null=True)),
                ('cvt', models.CharField(blank=True, max_length=200, null=True)),
                ('cassette', models.CharField(blank=True, max_length=200, null=True)),
                ('chainring', models.CharField(blank=True, max_length=200, null=True)),
                ('belt_drive', models.CharField(blank=True, max_length=200, null=True)),
                ('headset', models.CharField(blank=True, max_length=200, null=True)),
                ('stem', models.CharField(blank=True, max_length=200, null=True)),
                ('handlebar', models.CharField(blank=True, max_length=200, null=True)),
                ('grips', models.CharField(blank=True, max_length=200, null=True)),
                ('seatpost', models.CharField(blank=True, max_length=200, null=True)),
                ('seatpost_diameter', models.CharField(blank=True, max_length=200, null=True)),
                ('saddle', models.CharField(blank=True, max_length=200, null=True)),
                ('pedals', models.CharField(blank=True, max_length=200, null=True)),
                ('brake_type', models.CharField(blank=True, max_length=200, null=True)),
                ('front_brake', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_brake', models.CharField(blank=True, max_length=200, null=True)),
                ('motor_type', models.CharField(blank=True, max_length=200, null=True)),
                ('motor', models.CharField(blank=True, max_length=200, null=True)),
                ('additional_motors', models.CharField(blank=True, max_length=200, null=True)),
                ('motor_nominal_output', models.CharField(blank=True, max_length=200, null=True)),
                ('display', models.CharField(blank=True, max_length=200, null=True)),
                ('smart_bike', models.CharField(blank=True, max_length=200, null=True)),
                ('theft_gps', models.CharField(blank=True, max_length=200, null=True)),
                ('battery_watt_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('battery', models.CharField(blank=True, max_length=200, null=True)),
                ('charger', models.CharField(blank=True, max_length=200, null=True)),
                ('headlight', models.CharField(blank=True, max_length=200, null=True)),
                ('taillight', models.CharField(blank=True, max_length=200, null=True)),
                ('fenders', models.CharField(blank=True, max_length=200, null=True)),
                ('front_rack', models.CharField(blank=True, max_length=200, null=True)),
                ('rear_rack', models.CharField(blank=True, max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_specification_review', to='core.review')),
            ],
            options={
                'verbose_name': 'Review Specification',
                'verbose_name_plural': 'Review Specifications',
                'db_table': 'review_specification',
            },
        ),
    ]
