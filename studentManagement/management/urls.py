from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),

    path('rules/',views.rules,name="rules"),
    path('change_rules/',views.change_rules,name="change_rules"),

    path('students/<str:pk_test>',views.students,name="students"),
    path('grade/',views.grade,name="grade"),
    path('create_grade', views.create_grade, name="create_grade"),
    path('remove_grade/<str:pk>/', views.remove_grade, name="remove_grade"),
    path('update_grade/<str:pk>/', views.update_grade, name="update_grade"),
    path('subject_summary/',views.subject_summary,name="subject_summary"),
    path('final_summary/',views.final_summary,name="final_summary"),
    path('class_manage/',views.class_manage,name="class_manage"),
    path('maintenance/', views.maintenance, name='maintenance'),
]
handler404 = 'management.views.handler404'