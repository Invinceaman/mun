# Generated by Django 2.2.3 on 2019-10-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190701_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='driver_form',
            field=models.FileField(null=True, upload_to='mcmunc/'),
        ),
    ]
