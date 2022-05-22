from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main.html')

def login(request):
    return render(request,'login.html')
 
def logout(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def rules(request):
    return render(request,'viewRules.html')
 
def change_rules(request):
    return render(request,'changeRules.html') 

def students(request,pk_test):
    student=Student.object.get(id=pk_test)
    return render(request,'students.html') 


def insert_grade(request):
    return render(request, 'insert_grade.html')

def subject_summary(request):
    return render(request, 'subject_summary.html')

def final_summary(request):
    return render(request, 'final_summary.html')