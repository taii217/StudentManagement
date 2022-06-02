from django.contrib.auth.models import User

from management.models import Subject,Mark, Year
def createUserStudent():
    pass

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