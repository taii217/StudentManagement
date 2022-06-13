from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Mark, Rule, Student, Subject, Teacher, Class


class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'
        exclude = []


class studentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['ID']
        widgets = {
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
				attrs={'type': 'date'}
				),
        }

class classForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        exclude = ['Quantity']

class teacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['ID']

class subjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class RuleForm(ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
