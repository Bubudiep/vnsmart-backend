# Generated by Django 5.0.1 on 2024-02-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=224)),
                ('userpass', models.TextField(max_length=254)),
                ('userpass2', models.TextField(max_length=254)),
                ('email', models.TextField(max_length=254)),
                ('phone', models.TextField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
