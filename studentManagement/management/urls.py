from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.register, name="register"),
    
    path('rules/',views.rules,name="rules"),
    path('change_rules/',views.change_rules,name="change_rules"),

    path('student/<str:pk>',views.student,name="student"),
    path('students/',views.students,name="students"),

    path('teacher/<str:pk>',views.teacher,name="teacher"),
    path('teachers/',views.teachers,name="teachers"),

    path('grade/',views.grade,name="grade"),
    path('create_grade/', views.create_grade, name="create_grade"),
    path('remove_grade/<str:pk>/', views.remove_grade, name="remove_grade"),
    path('update_grade/<str:pk>/', views.update_grade, name="update_grade"),

    path('subject_summary/',views.subject_summary,name="subject_summary"),
    path('final_summary/',views.final_summary,name="final_summary"),

    path('classInfor/<str:pk>',views.class_Information,name="class_Information"),
    path('class_manage/',views.class_manage,name="class_manage"),
    
    path('maintenance/', views.maintenance, name='maintenance'),

    path('addStudent/', views.addStudent, name='addStudent'),
    path('addTeacher/', views.addTeacher, name='addTeacher'),
    # path('do/',views.do)
]
handler404 = 'management.views.handler404'