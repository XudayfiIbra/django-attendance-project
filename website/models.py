from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    code = models.IntegerField(unique=True)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Attendance')
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.CharField(max_length=20, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ],
    blank=True,
    null=True
    )
    
    


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
