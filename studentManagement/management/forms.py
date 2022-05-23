from django.forms import ModelForm
from .models import Mark

class MarkForm(ModelForm):
	class Meta:
			model = Mark
			fields = '__all__'