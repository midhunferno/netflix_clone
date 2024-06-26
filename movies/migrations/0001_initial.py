# Generated by Django 5.0.6 on 2024-05-24 16:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='movies')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('type', models.CharField(choices=[('seasonal', 'seasonal'), ('single', 'single')], max_length=10)),
                ('image', models.ImageField(upload_to='cover')),
                ('agel_limit', models.CharField(choices=[('All', 'All'), ('Kids', 'Kids')], max_length=15)),
                ('video', models.ManyToManyField(to='movies.videos')),
            ],
        ),
    ]
