# Generated by Django 4.0.3 on 2022-03-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_parkingslots'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.BigIntegerField(default=0)),
                ('laoding', models.BooleanField(default=False)),
                ('vehicle_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.vehiclecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homepage.basemodel')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], default='PENDING', max_length=255)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.event')),
                ('parking_slot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.parkingslots')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.vehicle')),
            ],
            bases=('homepage.basemodel',),
        ),
    ]
