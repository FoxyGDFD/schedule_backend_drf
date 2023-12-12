from rest_framework.routers import DefaultRouter
from apps.schedule.api.ViewSets import *
from django.apps import apps


router = DefaultRouter()

router.register('classroom', Classroom)
router.register('cathedra', Cathedra)
router.register('exam', Exam)
router.register('direction', Direction)
router.register('faculty', Faculty)
router.register('group', Group)
router.register('lesson', Lesson)
router.register('lesson-number', LessonNumber)
router.register('lesson-type', LessonType)
router.register('subject', Subject)
router.register('teacher', Teacher)
