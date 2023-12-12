from django.contrib import admin
from apps.schedule.models import *
import project_config


admin.site.site_header = project_config.ADMIN_SITE_HEADER

admin.site.register(Cathedra)
admin.site.register(Classroom)
admin.site.register(Direction)
admin.site.register(Exam)
admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(LessonNumber)
admin.site.register(LessonType)
admin.site.register(Subject)
admin.site.register(Teacher)