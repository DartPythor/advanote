# Generated by Django 4.2 on 2023-12-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0006_alter_task_priority_delete_mainimage_delete_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
    ]


__all__ = ()
