# Generated by Django 2.1.2 on 2018-12-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0006_tempmodel_humidity'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('water_level', models.FloatField(max_length=10)),
            ],
        ),
    ]
