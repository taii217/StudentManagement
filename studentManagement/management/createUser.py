from django.contrib.auth.models import User
from .models import *
import datetime

from management.models import Subject,Mark, Year
def createUserStudentID():
    now = datetime.datetime.now().year - 2000
    if(Student.objects.last()):
        IDlast = int(Student.objects.last().ID[2:]) + 1
    else :
        IDlast = 1
    id = str(now) + str(IDlast)
    return id

def createUserTeacherID():
    if(Teacher.objects.last()):
        IDlast = int(Teacher.objects.last().ID) + 1
    else: 
        return str(1)
    return IDlast

def DefaultMark(ID):
    subject = Subject.objects.all()
    year = Year.objects.last()
    s1 = Semeter.objects.first()
    s2 = Semeter.objects.last()
    for sub in subject:
        mark = Mark.objects.create()
        mark.Mark15 = 0
        mark.Mark60 = 0
        mark.MarkFinal = 0
        mark.semester = s1
        mark.year_school = year
        mark.StudentID = ID
        mark.SubjectID = sub
        mark.save()
    for sub in subject:
        mark = Mark.objects.create()
        mark.Mark15 = 0
        mark.Mark60 = 0
        mark.MarkFinal = 0
        mark.semester = s2
        mark.year_school = year
        mark.StudentID = ID
        mark.SubjectID = sub
        mark.save()

    Rp1 = Report_Class.objects.create()
    Rp1.StudentID = ID
    Rp1.mark = 0
    Rp1.semester = s1
    Rp1.year_school = year
    Rp1.save()

    Rp2 = Report_Class.objects.create()
    Rp2.StudentID = ID
    Rp2.mark = 0
    Rp2.semester = s2
    Rp2.year_school = year
    Rp2.save()

    return True

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
def checkInfo(instance):
    rule = Rule.objects.last()
    if not instance.Birthday :
        messages.error(request,'age is not suitable')
        return False
    age = calculate_age(instance.Birthday)
    if age >= rule.MinAge and age <= rule.MaxAge : 
        print(rule.MinAge)
        print(rule.MaxAge)
        return True
        
        
    return False
    
    