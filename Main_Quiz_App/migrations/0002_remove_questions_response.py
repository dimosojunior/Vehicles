# Generated by Django 4.2.6 on 2024-02-10 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Quiz_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='response',
        ),
    ]
