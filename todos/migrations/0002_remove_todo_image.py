# Generated by Django 3.2.17 on 2023-02-27 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='image',
        ),
    ]