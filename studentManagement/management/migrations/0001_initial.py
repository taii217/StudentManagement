# Generated by Django 4.0.4 on 2022-06-03 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField(blank=True, default=33, null=True)),
                ('More', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MinAge', models.IntegerField(blank=True, default=15, null=True)),
                ('MaxAge', models.IntegerField(blank=True, default=20, null=True)),
                ('MaxQuantity', models.IntegerField(blank=True, default=3, null=True)),
                ('ClassNumber', models.IntegerField(blank=True, default=9, null=True)),
                ('SubjectNumber', models.IntegerField(blank=True, default=9, null=True)),
                ('PassMark', models.FloatField(blank=True, default=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=10, null=True)),
                ('Birthday', models.DateTimeField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Classname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.class')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('school_year', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=10, null=True)),
                ('Birthday', models.DateTimeField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(max_length=10, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('SubjectID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.subject')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.student')),
                ('TeacherID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.FloatField(null=True)),
                ('Semester', models.IntegerField(blank=True, null=True)),
                ('StudentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.student')),
                ('SubjectID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.subject')),
                ('year_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.year')),
            ],
        ),
        migrations.CreateModel(
            name='Class_Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.class')),
                ('TeacherID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='HeadTeacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='school_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.year'),
        ),
    ]
