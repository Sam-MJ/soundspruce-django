# Generated by Django 5.0.6 on 2024-06-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='demo_video',
            field=models.URLField(blank=True),
        ),
    ]
