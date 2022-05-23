from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import MarkForm

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

def grade(request):
    grade = Mark.objects.all()
    return render(request, 'grade.html', {'grade':grade})
 
def create_grade(request):
    form = MarkForm()

    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/grade')

    context = {'form':form}
    return render(request, 'mark_form.html', context)

def update_grade(request, pk):
    mark = Mark.objects.get(id=pk)
    form = MarkForm(instance=mark)

    if request.method == 'POST':
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            return redirect('/grade')

    context = {'form':form}
    return render(request, 'mark_form.html', context)

def remove_grade(request, pk):
    grade = Mark.objects.get(id=pk)
    if request.method == "POST":
        grade.delete()
        return redirect('/grade')

    context = {'item':grade}
    return render(request, 'remove.html', context)

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