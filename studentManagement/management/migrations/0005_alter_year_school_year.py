# Generated by Django 4.0.4 on 2022-06-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_semeter_semeter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='school_year',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]