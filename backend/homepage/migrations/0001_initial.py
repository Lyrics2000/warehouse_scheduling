# Generated by Django 4.0.3 on 2022-03-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('PICKUP', 'PICKUP'), ('LORRY', 'LORRY'), ('TRANSIST', 'TRANSIST')], default='PICKUP', max_length=255)),
                ('vehicle_description', models.TextField()),
            ],
        ),
    ]
