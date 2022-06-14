from ast import Return

from management.forms import subjectForm
from management.models import Rule, Subject


def checkInfoClass(instance):
    ID = instance.ID[0:2]
    if ID == '10' or ID == '11' or ID == '12' : 
        return True
    return False

def checkInfoSubject():
    subNumber = Subject.objects.all().count()
    if subNumber >= Rule.objects.last().SubjectNumber:
        return False
    return True
