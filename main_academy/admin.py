from django.contrib import admin

from django.contrib import admin
from .models import Teacher, Course, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "date_of_birth", "user")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "description", "start_date", "end_date")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "date_of_birth", "url_link")

    def get_courses(self, obj):
        return ", ".join(course.name for course in obj.course.all())

    get_courses.short_description = "Courses"
