# Generated by Django 5.0 on 2023-12-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schoolapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="phone",
            field=models.TextField(),
        ),
    ]
