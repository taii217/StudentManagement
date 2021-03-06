# Generated by Django 4.0.4 on 2022-06-04 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_teacher',
            name='StudentID',
        ),
        migrations.RemoveField(
            model_name='student_teacher',
            name='TeacherID',
        ),
        migrations.RemoveField(
            model_name='class',
            name='More',
        ),
        migrations.AlterField(
            model_name='class',
            name='HeadTeacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.teacher'),
        ),
        migrations.DeleteModel(
            name='Class_Teacher',
        ),
        migrations.DeleteModel(
            name='Student_Teacher',
        ),
    ]
