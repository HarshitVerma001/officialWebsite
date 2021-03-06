# Generated by Django 2.2.10 on 2020-05-15 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("members", "0012_auto_20200202_1332"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField()),
                ("name", models.CharField(max_length=128)),
                ("published", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="PodcastGuest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("organisation", models.CharField(max_length=128)),
                ("about", models.CharField(max_length=128)),
                ("image", models.ImageField(blank=True, upload_to="podcast_guest/")),
            ],
        ),
        migrations.CreateModel(
            name="PodcastSeries",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("note", models.CharField(max_length=1000)),
                ("logo", models.ImageField(upload_to="podcast_image")),
                ("hosted", models.ManyToManyField(to="members.Member")),
            ],
        ),
        migrations.CreateModel(
            name="PodcastGuestLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "guest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="podcast.PodcastGuest",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Podcast",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("no", models.PositiveIntegerField()),
                ("recorded_on", models.DateTimeField(null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("published", models.BooleanField(default=True)),
                (
                    "guest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="podcast.PodcastGuest",
                    ),
                ),
                (
                    "series",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="podcast.PodcastSeries",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PodcastLink",
            fields=[
                (
                    "link_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="podcast.Link",
                    ),
                ),
                (
                    "podcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="podcast.Podcast",
                    ),
                ),
            ],
            bases=("podcast.link",),
        ),
    ]
