# Generated by Django 5.0 on 2023-12-08 14:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schoolapp", "0004_rename_name_department_department_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="department",
            new_name="department_id",
        ),
    ]
