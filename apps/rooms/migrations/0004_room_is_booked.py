# Generated by Django 5.0.3 on 2024-04-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_floor_floor_planning'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
