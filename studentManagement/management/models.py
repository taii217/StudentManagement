from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Subject(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Name

class Teacher(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    ID = models.AutoField(primary_key=True)
    SubjectID = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    FirstName = models.CharField(max_length=50, null=True)
    LastName = models.CharField(max_length=10, null=True)
    Birthday = models.DateTimeField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.FirstName+' '+self.LastName

class Class(models.Model):
    ID = models.CharField(max_length=10, primary_key=True)
    # Grade = models.IntegerField(null=True)
    Quantity = models.IntegerField(null=True, blank=True, default=33)
    HeadTeacher = models.OneToOneField(Teacher, null=True, on_delete=models.CASCADE)
    More = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.ID





class Student(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    ID = models.CharField(max_length=20, primary_key=True)
    Classname = models.ForeignKey(Class, null=True, on_delete=models.SET_NULL)
    FirstName = models.CharField(max_length=50, null=True)
    LastName = models.CharField(max_length=10, null=True)
    Birthday = models.DateTimeField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ID




class Mark(models.Model):
    Type = models.CharField(max_length=10, null=True)
    Mark = models.FloatField(null=True)
    Semester = models.IntegerField(null=True, blank=True)
    StudentID = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    SubjectID = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    

class Class_Teacher(models.Model):
    Classname = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)


class Student_Teacher(models.Model):
    StudentID = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)



class Rule(models.Model):
    MinAge = models.IntegerField(null=True, blank=True, default=15)
    MaxAge = models.IntegerField(null=True, blank=True, default=20)
    # Max number of member in a class
    MaxQuantity = models.IntegerField(null=True, blank=True, default=3)
    # Max number of class
    ClassNumber = models.IntegerField(null=True, blank=True, default=9)
    # Max number of subject
    SubjectNumber = models.IntegerField(null=True, blank=True, default=9)
    # Standard mark for student to pass
    PassMark = models.FloatField(null=True, blank=True, default=5)
