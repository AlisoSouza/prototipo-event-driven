# Generated by Django 4.2.2 on 2023-06-29 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
