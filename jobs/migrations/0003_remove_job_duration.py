# Generated by Django 4.1.5 on 2023-01-17 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='duration',
        ),
    ]
