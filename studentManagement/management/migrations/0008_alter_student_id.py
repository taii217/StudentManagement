# Generated by Django 4.0.4 on 2022-06-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_mark_semester_mark_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.IntegerField(max_length=1, primary_key=True, serialize=False),
        ),
    ]
