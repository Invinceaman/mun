# Generated by Django 2.2.1 on 2019-06-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techmun', '0004_auto_20190620_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chair_photos/'),
        ),
    ]
