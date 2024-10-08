# Generated by Django 5.0.6 on 2024-06-06 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
