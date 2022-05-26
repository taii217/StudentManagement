from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Mark, Student, Teacher
from django.contrib.auth.models import User


class MarkForm(ModelForm):
	class Meta:
		model = Mark
		fields = '__all__'

class studentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class teacherForm(ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['ID']
		
