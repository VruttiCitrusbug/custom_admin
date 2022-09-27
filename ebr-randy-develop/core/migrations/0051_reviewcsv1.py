# Generated by Django 3.2.12 on 2022-07-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_delete_reviewcsv1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewCSV1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.TextField(blank=True, null=True)),
                ('Year', models.TextField(blank=True, null=True)),
                ('Brand', models.TextField(blank=True, null=True)),
                ('Model', models.TextField(blank=True, null=True)),
                ('Trim', models.TextField(blank=True, null=True)),
                ('MSRP', models.TextField(blank=True, null=True)),
                ('Class', models.TextField(blank=True, null=True)),
                ('Frame_Type', models.TextField(blank=True, null=True)),
                ('Frame', models.TextField(blank=True, null=True)),
                ('Weight', models.TextField(blank=True, null=True)),
                ('Load_Capacity', models.TextField(blank=True, null=True)),
                ('Suspension', models.TextField(blank=True, null=True)),
                ('Fork', models.TextField(blank=True, null=True)),
                ('Rear_Shock', models.TextField(blank=True, null=True)),
                ('Wheel_Size', models.TextField(blank=True, null=True)),
                ('Front_Wheel', models.TextField(blank=True, null=True)),
                ('Rear_Wheel', models.TextField(blank=True, null=True)),
                ('Front_Hub', models.TextField(blank=True, null=True)),
                ('Rear_Hub', models.TextField(blank=True, null=True)),
                ('Tires', models.TextField(blank=True, null=True)),
                ('Gears', models.TextField(blank=True, null=True)),
                ('Shift_Levers', models.TextField(blank=True, null=True)),
                ('Front_Derailleur', models.TextField(blank=True, null=True)),
                ('Crankset', models.TextField(blank=True, null=True)),
                ('Rear_Derailleur', models.TextField(blank=True, null=True)),
                ('Electronic_Shifting', models.TextField(blank=True, null=True)),
                ('Internally_Geared_Hub', models.TextField(blank=True, null=True)),
                ('Continually_Variable_Transmission', models.TextField(blank=True, null=True)),
                ('Cassette', models.TextField(blank=True, null=True)),
                ('Chainring', models.TextField(blank=True, null=True)),
                ('Belt_Drive', models.TextField(blank=True, null=True)),
                ('Headset', models.TextField(blank=True, null=True)),
                ('Stem', models.TextField(blank=True, null=True)),
                ('Handlebar', models.TextField(blank=True, null=True)),
                ('Grips', models.TextField(blank=True, null=True)),
                ('Seatpost', models.TextField(blank=True, null=True)),
                ('Seatpost_Diameter', models.TextField(blank=True, null=True)),
                ('Saddle', models.TextField(blank=True, null=True)),
                ('Pedals', models.TextField(blank=True, null=True)),
                ('Brake_Type', models.TextField(blank=True, null=True)),
                ('Front_Brake', models.TextField(blank=True, null=True)),
                ('Rear_Brake', models.TextField(blank=True, null=True)),
                ('Motor_Type', models.TextField(blank=True, null=True)),
                ('Motor', models.TextField(blank=True, null=True)),
                ('Additional_Motors', models.TextField(blank=True, null=True)),
                ('Motor_Nominal_Output', models.TextField(blank=True, null=True)),
                ('Display', models.TextField(blank=True, null=True)),
                ('Smart_Bike', models.TextField(blank=True, null=True)),
                ('Theft_GPS', models.TextField(blank=True, null=True)),
                ('Additional_Battery', models.TextField(blank=True, null=True)),
                ('Battery_Watt_Hrs', models.TextField(blank=True, null=True)),
                ('Battery', models.TextField(blank=True, null=True)),
                ('Charger', models.TextField(blank=True, null=True)),
                ('Lights', models.TextField(blank=True, null=True)),
                ('Fenders', models.TextField(blank=True, null=True)),
                ('Front_Rack', models.TextField(blank=True, null=True)),
                ('Rear_Rack', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'review_csv_1',
            },
        ),
    ]
