from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),
    path('rules/',views.rules,name="rules"),
    path('insert_grade/',views.insert_grade,name="insert_grade"),
    path('subject_summary/',views.subject_summary,name="subject_summary"),
    path('final_summary/',views.final_summary,name="final_summary"),
    path('maintenance/', views.maintenance, name='maintenance'),
]
handler404 = 'management.views.handler404'