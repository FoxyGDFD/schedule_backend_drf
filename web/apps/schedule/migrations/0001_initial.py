# Generated by Django 4.1.7 on 2023-04-11 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cathedra",
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
                (
                    "name",
                    models.CharField(
                        max_length=512, unique=True, verbose_name="Название кафедры"
                    ),
                ),
            ],
            options={
                "verbose_name": "Кафедра",
                "verbose_name_plural": "Кафедры",
            },
        ),
        migrations.CreateModel(
            name="Classroom",
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
                ("name", models.CharField(max_length=128, verbose_name="Номер")),
                ("floor", models.IntegerField(verbose_name="Этаж")),
            ],
            options={
                "verbose_name": "Аудитория",
                "verbose_name_plural": "Аудитории",
            },
        ),
        migrations.CreateModel(
            name="ClassroomType",
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
                (
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип аудитории",
                "verbose_name_plural": "Типы аудиторий",
            },
        ),
        migrations.CreateModel(
            name="Direction",
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
                (
                    "name",
                    models.TextField(
                        max_length=512, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=8, unique=True, verbose_name="Код направления"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип аудитории",
                "verbose_name_plural": "Типы аудиторий",
            },
        ),
        migrations.CreateModel(
            name="DirectionTrainingType",
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
                (
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Уровень направления подготовки",
                "verbose_name_plural": "Уровни направления подготовки",
            },
        ),
        migrations.CreateModel(
            name="Faculty",
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
                (
                    "name",
                    models.CharField(
                        max_length=512, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Факультет",
                "verbose_name_plural": "Факультеты",
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                (
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название"
                    ),
                ),
                ("course", models.IntegerField(verbose_name="Курс")),
                (
                    "direction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.direction",
                        verbose_name="Направление",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subgroups",
                        to="schedule.group",
                        verbose_name="Группа-родитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Факультет",
                "verbose_name_plural": "Факультеты",
            },
        ),
        migrations.CreateModel(
            name="Housing",
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
                (
                    "name",
                    models.CharField(
                        max_length=256, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "floors_quantity",
                    models.IntegerField(verbose_name="Количество этажей"),
                ),
            ],
            options={
                "verbose_name": "Корпус",
                "verbose_name_plural": "Корпуса",
            },
        ),
        migrations.CreateModel(
            name="LessonNumber",
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
                (
                    "number",
                    models.IntegerField(
                        unique=True, verbose_name="Порядковый номер пары"
                    ),
                ),
                (
                    "start_time",
                    models.TimeField(unique=True, verbose_name="Время начала"),
                ),
                (
                    "end_time",
                    models.TimeField(unique=True, verbose_name="Время окончания"),
                ),
            ],
            options={
                "verbose_name": "Номер пары",
                "verbose_name_plural": "Номера пар",
            },
        ),
        migrations.CreateModel(
            name="LessonType",
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
                (
                    "name",
                    models.CharField(
                        max_length=512, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип пары",
                "verbose_name_plural": "Типы пар",
            },
        ),
        migrations.CreateModel(
            name="Subject",
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
                (
                    "name",
                    models.CharField(
                        max_length=512, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Предмет",
                "verbose_name_plural": "Предметы",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("name", models.CharField(max_length=256, verbose_name="Имя")),
                ("surname", models.CharField(max_length=256, verbose_name="Фамилия")),
                (
                    "patronymic",
                    models.CharField(max_length=256, verbose_name="Отчество"),
                ),
                (
                    "photo",
                    models.ImageField(
                        null=True, upload_to="", verbose_name="Фотография"
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.faculty",
                        verbose_name="Факультет",
                    ),
                ),
            ],
            options={
                "verbose_name": "Преподаватель",
                "verbose_name_plural": "Преподаватели",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.classroom",
                        verbose_name="Аудитория",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.group",
                        verbose_name="Группа",
                    ),
                ),
                (
                    "lesson_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.lessontype",
                        verbose_name="Тип пары",
                    ),
                ),
                (
                    "number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.lessonnumber",
                        verbose_name="Номер пары",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.subject",
                        verbose_name="Предмет",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.teacher",
                        verbose_name="Преподаватель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пара",
                "verbose_name_plural": "Пары",
            },
        ),
        migrations.CreateModel(
            name="Exam",
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
                (
                    "date_and_time",
                    models.DateTimeField(verbose_name="Дата и время проведения"),
                ),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.classroom",
                        verbose_name="Аудитория",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.group",
                        verbose_name="Группа",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.subject",
                        verbose_name="Предмет",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.teacher",
                        verbose_name="Преподаватель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Экзамен",
                "verbose_name_plural": "Экзамены",
            },
        ),
        migrations.AddField(
            model_name="direction",
            name="training_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.directiontrainingtype",
                verbose_name="Уровень обучения",
            ),
        ),
        migrations.AddField(
            model_name="classroom",
            name="classroom_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="schedule.classroomtype",
                verbose_name="Тип",
            ),
        ),
        migrations.AddField(
            model_name="classroom",
            name="housing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="schedule.housing",
                verbose_name="Корпус",
            ),
        ),
    ]
