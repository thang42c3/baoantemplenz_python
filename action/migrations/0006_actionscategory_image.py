# Generated by Django 4.2.5 on 2023-10-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0005_alter_action_image_alter_action_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionscategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='imagine/'),
        ),
    ]
