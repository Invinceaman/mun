# Generated by Django 2.2.2 on 2019-07-01 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190629_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ecc',
            new_name='emergency_care_card',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='health',
            new_name='health_information',
        ),
    ]
