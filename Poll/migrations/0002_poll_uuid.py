# Generated by Django 5.0.6 on 2024-05-28 04:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]