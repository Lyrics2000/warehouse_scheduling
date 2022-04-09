# Generated by Django 4.0.3 on 2022-04-09 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_driver_driver_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclecategory',
            name='vehicle_description',
        ),
        migrations.AlterField(
            model_name='queue',
            name='parking_slot_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.parkingslots'),
        ),
    ]