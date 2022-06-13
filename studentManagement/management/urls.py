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

    path('grade/<str:pk>',views.grade,name="grade"),
    path('create_grade/<str:pk>', views.create_grade, name="create_grade"),
    path('remove_grade/<str:pk>/', views.remove_grade, name="remove_grade"),
    path('update_grade/<str:id>/<str:se>/', views.update_grade, name="update_grade"),

    path('classSummary/',views.classSummary, name="classSummary"),
    path('subjectSummary/<str:subjectID>',views.subjectSummary, name="subjectSummary"),
    path('report/',views.report, name="report"),


    path('classInfor/<str:pk>',views.class_Information,name="class_Information"),
    path('class_manage/',views.class_manage,name="class_manage"),
    path('delete_class/<str:pk>',views.delete_class,name="delete_class"),
    
    path('maintenance/', views.maintenance, name='maintenance'),

    path('addStudent/', views.addStudent, name='addStudent'),
    path('addTeacher/', views.addTeacher, name='addTeacher'),
    path('addTeacher/', views.addTeacher, name='addTeacher'),


    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),


    # path('do/',views.do)
]
handler404 = 'management.views.handler404'