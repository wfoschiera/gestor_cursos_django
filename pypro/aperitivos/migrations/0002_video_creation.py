# Generated by Django 3.2.5 on 2021-08-20 15:02
from datetime import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aperitivos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="creation",
            field=models.DateTimeField(auto_now_add=True, default=datetime.now()),
            preserve_default=False,
        ),
    ]
