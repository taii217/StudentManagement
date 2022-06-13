import email
from multiprocessing import context
from pydoc import classname
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .report import *
from .createUser import *
from .models import *
from .decorators import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
# Create your views here.
from .forms import MarkForm, RuleForm, studentForm, teacherForm,classForm,subjectForm
from .filters import ClassFilter, StudentFilter,TeacherFilter

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
    rule = Rule.objects.last()
    context = {'rule':rule}
    return render(request,'viewRules.html',context)

@login_required(login_url='login')  
@admin_only
def change_rules(request):
    rule = Rule.objects.last()
    if request.method == "POST":
        rule.MinAge = request.POST.get('MinAge')
        rule.MaxAge = request.POST.get('MaxAge')
        rule.MaxQuantity = request.POST.get('NumMen')
        rule.ClassNumber = request.POST.get('NumGrades')
        rule.SubjectNumber = request.POST.get('NumSubject')
        rule.PassMark = request.POST.get('GPA')
        rule.save()
        return redirect('/rules')
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
    teachers=Teacher.objects.all()
    myFilter = TeacherFilter(request.GET, queryset=teachers)
    teachers=myFilter.qs
    context={'teachers':teachers,'myFilter': myFilter}
    return render(request,'teachers.html',context) 

@login_required(login_url='login')
def student(request,pk):
    student=Student.objects.get(ID=pk)

    context={'student':student}
    return render(request,'student.html',context) 

@login_required(login_url='login')
@groups_only('Admin','Teachers')
def students(request):
    year = Year.objects.last()
    students=Student.objects.all()
    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs 
    for s in students:
        s.rp1 = round(Report_Class.objects.get(StudentID = s.ID,semester = 1,year_school = year).mark,2)
        s.rp2 = round(Report_Class.objects.get(StudentID = s.ID,semester = 2,year_school = year).mark,2)

    
    context={'students':students,'myFilter': myFilter}

    return render(request,'students.html',context) 

@login_required(login_url='login')
def grade(request,pk):
    year = Year.objects.last()
    grade1 = Mark.objects.filter(StudentID = pk,year_school = year, semester = 1)
    grade2 = Mark.objects.filter(StudentID = pk,year_school = year, semester = 2)
    avgMark1 = round(Report_Class.objects.get(StudentID = pk,semester = 1).mark,2)
    avgMark2 = round(Report_Class.objects.get(StudentID = pk,semester = 2).mark,2)
    context ={'grade1':grade1,'grade2':grade2,'id':pk,'year':year,'avg1':avgMark1,'avg2':avgMark2}
    return render(request, 'grade.html', context)
 
@login_required(login_url='login')
def create_grade(request,pk):
    # initial_dict = {
    #     "StudentID" : pk,
    #     "Semester"  : Semeter.objects.last(),
    #     "year_school" : Year.objects.last(),
    # }
    # form = MarkForm(initial = initial_dict)
    
    # if request.method == 'POST':
    #     form = MarkForm(request.POST,initial = initial_dict)
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.semester = 1
    #         instance.year_school = Year.objects.last()
    #         instance.save()
    #         messages.success(request,'SUCCESS')
    #         return HttpResponseRedirect(request.path_info)

    # context = {'form':form}
    return render(request, 'mark_form.html', context={})

@login_required(login_url='login')
def update_grade(request, id,se):
    mark = Mark.objects.get(id=id,semester = se,year_school = Year.objects.last())
    form = MarkForm(instance=mark)
    studentID_ = mark.StudentID
    year_ = mark.year_school
    sem_ = mark.semester
    Rp = Report_Class.objects.get(StudentID = studentID_,year_school = year_ ,semester = sem_)
    if request.method == 'POST':
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid(): 
            mark_condition1 = form.cleaned_data.get('Mark15')
            mark_condition2 = form.cleaned_data.get('Mark60') 
            mark_condition3 = form.cleaned_data.get('MarkFinal') 
            if isMarkValid(mark_condition1) and isMarkValid(mark_condition2) and isMarkValid(mark_condition3) :
                form.save()
                mt = Mark.objects.filter(StudentID = studentID_,year_school = year_,semester = sem_)
                #update report
                Rp.mark = ave_mark(mt)
                Rp.save()
                return redirect('/grade/'+ str(studentID_))
            else:
                messages.error(request,'Error : Mark <= 10 and > 0')

    context = {'form':form}
    return render(request, 'update_mark.html', context)

@login_required(login_url='login')
def remove_grade(request, pk):
    grade = Mark.objects.get(id=pk)
    studentID = grade.StudentID
    if request.method == "POST":
        grade.delete()
        return redirect('/grade/'+ str(studentID))

    context = {'item':grade}
    return render(request, 'remove.html', context)

@login_required(login_url='login')
def classSummary(request):
    year = Year.objects.last()
    cla = Class.objects.all() 
    for cl in cla:
        stu = Student.objects.filter(Classname = cl.ID)
        cl.numPass = 0
        for s in stu:
            rp1 = Report_Class.objects.get(StudentID = s.ID,semester = 1,year_school = year).mark
            rp2 = Report_Class.objects.get(StudentID = s.ID,semester = 2,year_school = year).mark
            if is_pass_GPA((rp1 + rp2*2)/3): 
                cl.numPass+=1
        if cl.Quantity == 0 : cl.rate = 0
        else : cl.rate = round(cl.numPass / cl.Quantity * 100,2)

    context = {"class":cla}
    return render(request, 'classSummary.html',context)

@login_required(login_url='login')
def subjectSummary(request,subjectID):
    year = Year.objects.last()
    cla1 = Class.objects.all() 
    cla2 = Class.objects.all() 
    subname = Subject.objects.get(ID = subjectID ).Name
    mark1 = Mark.objects.filter(SubjectID = subjectID,year_school = year,semester = 1)
    mark2 = Mark.objects.filter(SubjectID = subjectID,year_school = year,semester = 2)
    for cl,cl2 in zip(cla1,cla2):
        cl.numPass = 0
        cl2.numPass = 0
        for n,m in zip(mark1,mark2) :
            rp1 = ((n.Mark15 or 0) + (n.Mark60 or 0)*2  + (n.MarkFinal or 0 )*3)/6
            rp2 = ((m.Mark15 or 0) + (m.Mark60 or 0)*2  + (m.MarkFinal or 0 )*3)/6
            if is_pass_GPA(rp1): 
                cl.numPass +=1
            if is_pass_GPA(rp2): 
                cl2.numPass +=1
    
        if cl.Quantity == 0 : 
            cl.rate , cl2.rate = 0,0
        else : 
            cl.rate = round(cl.numPass / cl.Quantity * 100,2)
            cl2.rate = round(cl2.numPass / cl2.Quantity * 100,2)

    context = {"class1":cla1,"class2":cla2,"name":subname}
    return render(request, 'subjectSummary.html',context)

@login_required(login_url='login')
def class_Information(request, pk):
    year = Year.objects.last()
    class1= Class.objects.get(ID=pk)
    students = Student.objects.filter(Classname=pk)
    for s in students:
        s.rp1 = round(Report_Class.objects.get(StudentID = s.ID,semester = 1,year_school = year).mark,2)
        s.rp2 = round(Report_Class.objects.get(StudentID = s.ID,semester = 2,year_school = year).mark,2)
    class1.Quantity = students.count()
    class1.save()

    context={'class1':class1,'students':students}
    return render(request, 'classInfor.html', context)

@login_required(login_url='login')
def class_manage(request):
    Classes = Class.objects.all()
    #Years = Year.objects.all()

    myFilter = ClassFilter(request.GET, queryset=Classes)
    Classes = myFilter.qs

    context = {'Classes': Classes, 'myFilter': myFilter}
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
    ID = createUserStudentID()
    usern = "SV" + ID
    passd = ID
    form = studentForm()

    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if not checkInfo(instance):
                messages.error(request,'age is not suitable or class is Maxstudent')
            else :
                Email = form.cleaned_data.get('Email')
                user = get_user_model().objects.create_user(username=usern,email=Email,password=passd)
                group.user_set.add(user)
                instance.user = user
                instance.ID = ID
                updateQuantity(instance.Classname)
                instance.save()
                messages.success(request,'Success create ' + usern)
                DefaultMark(instance)
            return HttpResponseRedirect(request.path_info)
    context ={'form':form}
    return render(request,'addStudent.html',context)

@login_required(login_url='login')
@admin_only
def addTeacher(request):
    group = Group.objects.get(name='Teachers') 
    ID = createUserTeacherID()
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
            instance.ID = ID
            instance.save()
            messages.success(request,'Success create ' + usern)
            return HttpResponseRedirect(request.path_info)
    context ={'form':form}
    return render(request,'addTeacher.html',context)

@login_required(login_url='login')
@admin_only
def addClass(request):
    form = classForm()

    if request.method == 'POST':
        form = classForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.save()

            messages.success(request,'Success create ' + instance.ID)
            return HttpResponseRedirect(request.path_info)
    
    context ={'form':form}
    
    return render(request,'addClass.html',context)


@login_required(login_url='login')
@admin_only
def change_name_subjects(request):
    subject=Subject.objects.all()
    form = subjectForm()
    if request.method == 'POST':
        form = subjectForm(request.POST,instance=subject)
        if form.is_valid():
            return HttpResponseRedirect(request.path_info)
    context ={'form':form}
    return render(request,'change_name_subjects.html',context)

@groups_only('Admin','Teachers')
def report(request):
    sub = Subject.objects.all()
    context = {'subj':sub}
    return render(request,'report.html',context)


# def do(request):
#     teacher = Student.objects.last()
#     teacher.delete()
#     git('oke')
#     return render(request,'login.html')

