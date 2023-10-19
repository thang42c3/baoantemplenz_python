# Generated by Django 4.2.5 on 2023-10-11 02:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vn_name', models.CharField(max_length=255)),
                ('vn_slug', models.SlugField(max_length=250)),
                ('en_name', models.CharField(max_length=255)),
                ('en_slug', models.SlugField(max_length=250)),
                ('vn_description', models.TextField(blank=True, null=True)),
                ('en_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vn_name', models.CharField(max_length=255)),
                ('vn_slug', models.SlugField(max_length=250)),
                ('en_name', models.CharField(max_length=255)),
                ('en_slug', models.SlugField(max_length=250)),
                ('vn_description', models.TextField(blank=True, null=True)),
                ('en_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='imagine/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actionsCategory', to='aboutus.aboutuscategory')),
            ],
        ),
    ]
