# Generated by Django 3.2.5 on 2021-08-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Modulo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=64)),
                ("publico", models.TextField(null=True)),
                ("descricao", models.TextField(null=True)),
                ("order", models.PositiveIntegerField(db_index=True, editable=False, null=True, verbose_name="order")),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
