# Generated by Django 5.1.2 on 2024-10-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FarmerRegister",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="VentFindings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type_of_breed", models.CharField(max_length=100)),
                ("age", models.CharField(max_length=100)),
                ("type_of_disease", models.CharField(max_length=100)),
                ("symptoms", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("date", models.DateTimeField(max_length=100)),
            ],
        ),
    ]