# Generated by Django 2.2.3 on 2019-10-30 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191023_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='delegate_release',
        ),
        migrations.RemoveField(
            model_name='user',
            name='luggage_search',
        ),
    ]
