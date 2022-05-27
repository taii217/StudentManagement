# Generated by Django 4.0.4 on 2022-05-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_mark_semester_alter_rule_classnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='ClassNumber',
            field=models.IntegerField(blank=True, default=9, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='MaxAge',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='MinAge',
            field=models.IntegerField(blank=True, default=15, null=True),
        ),
    ]