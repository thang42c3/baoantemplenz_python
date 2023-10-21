# Generated by Django 4.2.5 on 2023-10-21 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_rename_en_address_contactinformation_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedialink',
            old_name='url',
            new_name='url_facebook',
        ),
        migrations.RemoveField(
            model_name='socialmedialink',
            name='description',
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='url_google_plus',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='url_instagram',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='url_linkedin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='url_twitter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
