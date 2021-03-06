# Generated by Django 2.0.1 on 2018-08-26 18:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('issue_date', models.DateTimeField()),
                ('new_class', models.CharField(max_length=255)),
                ('new_type', models.CharField(max_length=255)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'db_table': 'api_permitdata',
                'managed': False,
            },
        ),
    ]
