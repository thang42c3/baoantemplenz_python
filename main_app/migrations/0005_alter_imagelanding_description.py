# Generated by Django 4.2.5 on 2023-10-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_imagelanding_image_alter_imagelanding_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelanding',
            name='description',
            field=models.TextField(null=True),
        ),
    ]