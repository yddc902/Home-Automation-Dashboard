# Generated by Django 2.1.4 on 2018-12-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_watermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('water_level', models.FloatField(max_length=10)),
                ('water_detected', models.BooleanField()),
            ],
        ),
    ]
