# Generated by Django 4.1.7 on 2023-12-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0006_remove_exam_teacher_exam_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exam",
            name="group",
        ),
        migrations.AddField(
            model_name="exam",
            name="group",
            field=models.ManyToManyField(to="schedule.group", verbose_name="Группа"),
        ),
    ]
