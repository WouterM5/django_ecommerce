# Generated by Django 4.1.3 on 2022-11-27 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_variation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="variation",
            old_name="prpduct",
            new_name="product",
        ),
    ]