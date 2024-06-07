# Generated by Django 5.0.6 on 2024-06-07 07:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_poll_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]