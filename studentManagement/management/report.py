from .models import Rule

def ave_mark(mark):
    sum = 0
    num = 0
    for m in mark:
        if(m != 0): 
            sum+=m
            num+=1
    if num == 0: 
        return 0
    print(sum)
    print(num)
    print("oke")

    return sum/num

def is_pass_GPA(mark):
    GPA = Rule.objects.last().PassMark
    if (mark >= GPA ): 
        return True
    return False
