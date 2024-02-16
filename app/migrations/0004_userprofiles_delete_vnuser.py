# Generated by Django 5.0.1 on 2024-02-16 16:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_vnuser_username_remove_vnuser_userpass_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=224, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=254, null=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('comments', models.TextField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='VNUser',
        ),
    ]