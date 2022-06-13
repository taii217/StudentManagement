from django.forms import DecimalField
import django_filters  
from .models import *
from django_filters import DateFilter,CharFilter

class ClassFilter(django_filters.FilterSet):
    class Meta:
        model = Class
        fields = ['ID', 'school_year']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields =['ID','Classname','FirstName','LastName']
        
class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields =['ID','FirstName','LastName']
    # def my_custom_filter(self, queryset, name, value):
    #    return queryset.filter(**{
    #         name: value,
    #     }) 
    
        