# Generated by Django 4.0.4 on 2022-06-05 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_semeter_year_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='Semester',
        ),
        migrations.AddField(
            model_name='mark',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.semeter'),
        ),
    ]
