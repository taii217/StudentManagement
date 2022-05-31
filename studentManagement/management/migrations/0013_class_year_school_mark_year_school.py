# Generated by Django 4.0.3 on 2022-05-31 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='year_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.year'),
        ),
        migrations.AddField(
            model_name='mark',
            name='year_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.year'),
        ),
    ]
