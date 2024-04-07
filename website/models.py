from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    code = models.IntegerField(unique=True)

    
class Courses(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Attendance')
    code = models.IntegerField(unique=True)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('student', 'course')
    
    @classmethod
    def get_attendance_for_class(cls, class_id):
        return cls.objects.filter(student__enrollment__classes__id=class_id)


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
