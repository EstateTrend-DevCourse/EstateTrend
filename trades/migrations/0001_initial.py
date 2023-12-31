# Generated by Django 4.2.7 on 2023-11-09 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RealEstate",
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
                ("estate_name", models.CharField(max_length=200)),
                ("exclusive_area", models.FloatField(default=0.0)),
                ("year_of_construction", models.IntegerField(default=2000)),
                ("floor", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                ("base_address", models.CharField(max_length=200)),
                ("si_do_name", models.CharField(default="", max_length=200)),
                ("gu_gun_name", models.CharField(default="", max_length=200)),
                ("dong_name", models.CharField(default="", max_length=200)),
                ("region_code", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="RealEstateTrade",
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
                ("trade_price", models.IntegerField(default=0)),
                ("trade_year", models.IntegerField(default=2000)),
                ("trade_month", models.IntegerField(default=1)),
                ("trade_day", models.IntegerField(default=1)),
                (
                    "real_estate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="realestatetrades",
                        to="trades.realestate",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="realestate",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="realestates",
                to="trades.region",
            ),
        ),
    ]
