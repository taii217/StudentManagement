from django.contrib.auth.models import User
from .models import *
import datetime

from management.models import Subject,Mark, Year
def createUserStudentID():
    now = datetime.datetime.now().year - 2000
    if(Student.objects.last()):
        IDlast = int(Student.objects.last().ID) + 1
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
    for sub in subject:
        # init_data = {
        # 'Mark' : 0,
        # 'Semester' : 1,
        # 'year_school' : Year.objects.last(),
        # 'StudentID' : ID,
        # 'SubjectID' : sub.ID
        # }   
        mark = Mark.objects.create()
        mark.Mark = 0
        mark.Semester = 1
        mark.year_school = Year.objects.last()
        mark.StudentID = ID
        mark.SubjectID = sub
        mark.save()
    return True