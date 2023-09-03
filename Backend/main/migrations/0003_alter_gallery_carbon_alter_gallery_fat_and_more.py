# Generated by Django 4.2 on 2023-06-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_food_options_alter_gallery_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="carbon",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="fat",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="food_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="image_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="kcal",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="pro",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="total",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]