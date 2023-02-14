# Generated by Django 4.1.7 on 2023-02-14 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(limit_value=3)])),
            ],
        ),
    ]
