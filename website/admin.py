from django.contrib import admin
from .models import Attendance, Student, Courses, Instructor

class studentAdmin(admin.ModelAdmin):
    list_display = ("name","email", "code", "sex",)

admin.site.register(Student, studentAdmin)

class attendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "date", "is_present",)
    
admin.site.register(Attendance, attendanceAdmin)

class coursesAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)
admin.site.register(Courses, coursesAdmin)

class instructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', "sex",)

admin.site.register(Instructor, instructorAdmin)
