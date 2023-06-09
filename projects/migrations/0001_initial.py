# Generated by Django 4.1.7 on 2023-03-25 12:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=2550, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2550, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.UUID('3c0d8abe-fc97-4bb7-9309-bee193a1c2f5'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
