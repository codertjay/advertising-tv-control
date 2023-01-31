# Generated by Django 4.1.5 on 2023-01-31 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Broadcast",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "media",
                    models.FileField(blank=True, null=True, upload_to="broadcasts/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BroadcastInTv",
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
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("duration", models.FloatField(default=20.0)),
                ("order", models.IntegerField(default=10)),
                ("active", models.BooleanField(default=True)),
                (
                    "broadcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tv.broadcast"
                    ),
                ),
            ],
            options={"ordering": ["order"],},
        ),
        migrations.CreateModel(
            name="Tv",
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
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "broadcasts",
                    models.ManyToManyField(
                        blank=True,
                        related_name="tv",
                        through="tv.BroadcastInTv",
                        to="tv.broadcast",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="broadcastintv",
            name="tv",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tv.tv"
            ),
        ),
    ]
