from django.test import TestCase
from matplotlib import path
from . import views
# Create your tests here.
urlpatterns = [
    path('', views.home,name="home"),
]