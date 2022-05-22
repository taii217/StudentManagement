from django.shortcuts import render
from .models import Student
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
    student=Student.objects.get(ID=pk_test)
    return render(request,'students.html') 

 
def insert_grade(request):
    return render(request, 'insert_grade.html')

def subject_summary(request):
    return render(request, 'subject_summary.html')

def final_summary(request):
    return render(request, 'final_summary.html')

def class_manage(request):
    return render(request, 'classManage.html')

def handler404(request, exception):
    return render(request, '404.html')

def maintenance(request):
    return render(request, 'maintenance.html')