# Generated by Django 4.1.3 on 2022-11-02 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slopes", "0002_slope_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slopeupdate",
            name="slope",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="updates",
                to="slopes.slope",
            ),
        ),
    ]
