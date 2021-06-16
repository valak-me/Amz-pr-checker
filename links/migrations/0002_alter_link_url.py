# Generated by Django 3.2.2 on 2021-06-05 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
