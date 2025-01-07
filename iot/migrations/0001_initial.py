# Generated by Django 5.1.4 on 2025-01-07 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Valve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valve_no', models.IntegerField()),
                ('opening_time', models.DateTimeField(auto_now_add=True)),
                ('tank_level', models.DecimalField(decimal_places=2, max_digits=8)),
                ('flow_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('soil_moisture', models.IntegerField()),
                ('soil_temperature', models.DecimalField(decimal_places=2, max_digits=8)),
                ('closing_time', models.DateTimeField(auto_now_add=True)),
                ('is_open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisture', models.IntegerField()),
                ('tank_level', models.DecimalField(decimal_places=2, max_digits=8)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valve_open_time', models.DateTimeField(auto_now_add=True)),
                ('valve_close_time', models.DateTimeField(auto_now=True)),
                ('valve', models.ForeignKey(limit_choices_to={'valve_no__in': [1, 2]}, on_delete=django.db.models.deletion.CASCADE, to='iot.valve')),
            ],
        ),
    ]