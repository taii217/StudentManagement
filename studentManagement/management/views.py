import email
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import *
from .decorators import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
# Create your views here.
from .forms import MarkForm, RuleForm, studentForm, teacherForm

def register(request):
    context = {}
    return render(request,'register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.info(request,'User or password is incorrect')
    context ={}
    return render(request,'login.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request,'main.html')

@login_required(login_url='login')
def rules(request):
    rule = Rule.objects.first()
    context = {'rule':rule}
    return render(request,'viewRules.html',context)

@login_required(login_url='login')  
@admin_only
def change_rules(request):
    rule = Rule.objects.last()
    # form = RuleForm()
    # if request.method == 'POST':
    #     form = RuleForm(request.POST)
    #     if form.is_valid:
    #         instance = form.save()
    context = {'rule':rule}
    return render(request,'changeRules.html',context) 

@login_required(login_url='login')
@admin_only
def teacher(request,pk):
    teacher=Teacher.objects.get(ID=pk)
    context={'teacher':teacher}
    return render(request,'teacher.html',context) 

@login_required(login_url='login')
@admin_only
def teachers(request):
    teachers=Teacher.objects.all().order_by('ID') 
    context={'teachers':teachers}
    return render(request,'teachers.html',context) 

@login_required(login_url='login')
def student(request,pk):
    student=Student.objects.get(ID=pk)
    context={'student':student}
    return render(request,'student.html',context) 

@login_required(login_url='login')
@groups_only('Admin','Teachers')
def students(request):
    students=Student.objects.all().order_by('ID') 
    context={'students':students}
    return render(request,'students.html',context) 

@login_required(login_url='login')
def grade(request,pk):
    year = Year.objects.last()
    grade = Mark.objects.filter(StudentID = pk,year_school = year )
    return render(request, 'grade.html', {'grade':grade,'id':pk,'year':year})
 
@login_required(login_url='login')
def create_grade(request,pk):
    initial_dict = {
        "StudentID" : pk,
        "Semester"  : 1,
        "year_school" : Year.objects.last().year_school,
    }
    form = MarkForm(initial = initial_dict)
    
    if request.method == 'POST':
        form = MarkForm(request.POST,initial = initial_dict)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Semester = 1
            instance.year_school = Year.objects.last()
            instance.save()
            messages.success(request,'SUCCESS')
            return HttpResponseRedirect(request.path_info)

    context = {'form':form}
    return render(request, 'mark_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def remove_grade(request, pk):
    grade = Mark.objects.get(id=pk)
    if request.method == "POST":
        grade.delete()
        return redirect('/grade')

    context = {'item':grade}
    return render(request, 'remove.html', context)

@login_required(login_url='login')
def subject_summary(request):
    return render(request, 'subject_summary.html')

@login_required(login_url='login')
def final_summary(request):
    return render(request, 'final_summary.html')

@login_required(login_url='login')
def class_Information(request, pk):
    class1= Class.objects.get(ID=pk)
    students = Student.objects.filter(Classname=pk)
    class1.Quantity = students.count()
    class1.save()
    context={'class1':class1,'students':students}
    return render(request, 'classInfor.html', context)

@login_required(login_url='login')
def class_manage(request):
    Classes = Class.objects.all()
    Years = Year.objects.all()
    context = {'Classes': Classes,'Years': Years}
    return render(request, 'classManage.html', context)

@login_required(login_url='login')
def delete_class(request, pk):
    class1=Class.objects.get(ID=pk)
    if request.method == 'POST':
        class1.delete()
        return redirect('/class_manage')
    
    context = {'class1':class1}
    return render(request, 'deleteClass.html', context)

def handler404(request, exception):
    return render(request, '404.html')

def maintenance(request):
    return render(request, 'maintenance.html')

@login_required(login_url='login')
@admin_only
def addStudent(request):
    group = Group.objects.get(name='Students') 
    if(Student.objects.last()):
        ID = Student.objects.last().ID + 1
    else:
        ID = 0
    usern = "SV" + str(ID)
    passd = str(ID)
    form = studentForm()

    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            Email = form.cleaned_data.get('Email')
            user = get_user_model().objects.create_user(username=usern,email=Email,password=passd)
            group.user_set.add(user)
            instance.user = user
            instance.save()
            messages.success(request,'SUCCESS')
            return HttpResponseRedirect(request.path_info)
    context ={'form':form}
    return render(request,'addStudent.html',context)

@login_required(login_url='login')
@admin_only
def addTeacher(request):
    group = Group.objects.get(name='Teachers') 
    ID = Teacher.objects.all().count() + 1
    usern = "TC" + str(ID)
    passd = str(ID)
    form = teacherForm()

    if request.method == 'POST':
        form = teacherForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            Email = form.cleaned_data.get('Email')
            user = get_user_model().objects.create_user(username=usern,email=Email,password=passd)
            group.user_set.add(user)
            instance.user = user
            instance.save()
            messages.success(request,'SUCCESS')
            return HttpResponseRedirect(request.path_info)
    context ={'form':form}
    return render(request,'addTeacher.html',context)

# def do(request):
#     teacher = Student.objects.last()
#     teacher.delete()
#     print('oke')
#     return render(request,'login.html')

