# Generated by Django 4.2.5 on 2023-10-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_aboutuscategory_menu_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelanding',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
