# Generated by Django 4.2.3 on 2023-09-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='if_done',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]