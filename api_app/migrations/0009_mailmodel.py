# Generated by Django 2.1.2 on 2019-01-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0008_detectionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('mail_detected', models.BooleanField()),
            ],
        ),
    ]
