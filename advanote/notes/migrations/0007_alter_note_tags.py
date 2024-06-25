# Generated by Django 4.2 on 2023-12-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tag", "0002_alter_tag_name"),
        ("notes", "0006_alter_note_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="note_tags",
                to="tag.tag",
                verbose_name="теги",
            ),
        ),
    ]


__all__ = ()
