# Generated by Django 3.0 on 2019-12-12 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20191209_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='page',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
