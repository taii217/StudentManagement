# Generated by Django 4.0.3 on 2022-05-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_student_user_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
