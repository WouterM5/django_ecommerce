# Generated by Django 4.1.3 on 2022-11-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_remove_product_image_product_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="images",
            field=models.ImageField(default=None, upload_to="photos/products"),
        ),
    ]
