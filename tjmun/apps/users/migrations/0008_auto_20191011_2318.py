# Generated by Django 2.2.3 on 2019-10-12 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191011_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emergency_care_card',
            field=models.FileField(null=True, upload_to='ecc_forms/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='health_information',
            field=models.FileField(null=True, upload_to='health_forms/'),
        ),
    ]