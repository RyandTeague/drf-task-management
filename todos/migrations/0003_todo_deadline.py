# Generated by Django 3.2.17 on 2023-02-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_options_todo_created_at_todo_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
