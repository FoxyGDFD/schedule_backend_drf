# Generated by Django 4.1.7 on 2023-12-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0003_rename_groups_group_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="week_day",
            field=models.CharField(
                choices=[
                    ("Понедельник", "monday"),
                    ("Вторник", "tuesday"),
                    ("Среда", "wednesday"),
                    ("Четверг", "thursday"),
                    ("Пятница", "friday"),
                    ("Суббота", "saturday"),
                ],
                default="Понедельник",
                max_length=11,
                verbose_name="День недели",
            ),
        ),
    ]