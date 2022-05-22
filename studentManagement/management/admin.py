from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Mark)
admin.site.register(Student_Teacher)
admin.site.register(Class_Teacher)
admin.site.register(Rule)
