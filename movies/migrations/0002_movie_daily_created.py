# Generated by Django 4.0.3 on 2023-01-31 04:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='daily_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
