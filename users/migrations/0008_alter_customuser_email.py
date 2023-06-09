# Generated by Django 4.1.7 on 2023-03-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_customuser_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
