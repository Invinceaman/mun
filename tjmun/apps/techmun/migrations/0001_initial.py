# Generated by Django 2.2.1 on 2019-05-24 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')])),
                ('delegationaward', models.CharField(max_length=20)),
                ('committees', models.ManyToManyField(related_name='conference', to='awards.Committee')),
            ],
        ),
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('award', models.CharField(max_length=20)),
                ('gavel', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric, dashes, and underscores allowed', regex='^[a-zA-Z0-9_\\-]+$')])),
                ('conferences', models.ManyToManyField(related_name='year', to='awards.Conference')),
            ],
        ),
        migrations.AddField(
            model_name='committee',
            name='delegations',
            field=models.ManyToManyField(related_name='committee', to='awards.Delegation'),
        ),
    ]
