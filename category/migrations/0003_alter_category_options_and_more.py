# Generated by Django 4.1.3 on 2022-11-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0002_alter_category_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.RenameField(
            model_name="category",
            old_name="category_image",
            new_name="cat_image",
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
