# Generated by Django 2.2.3 on 2019-12-08 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20191029_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code_of_conduct',
        ),
        migrations.RemoveField(
            model_name='user',
            name='parent_authorization',
        ),
    ]
