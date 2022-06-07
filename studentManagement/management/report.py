from .models import Rule

def ave_mark(mark):
    sum = 0
    num = 0
    for m in mark:
        sum += (float(m.Mark15 or 0) + float(m.Mark60 or 0) * 2 + float(m.MarkFinal or 0) * 3)/6
        num+=1
    return sum/num

def is_pass_GPA(mark):
    GPA = Rule.objects.last().PassMark
    if (mark >= GPA ): 
        return True
    return False

def isMarkValid(mark):
    if (mark <= 10 and mark >= 0):
        return True
    return False
