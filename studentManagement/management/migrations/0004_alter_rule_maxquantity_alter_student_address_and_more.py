# Generated by Django 4.0.3 on 2022-05-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_rule_classnumber_alter_rule_maxage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='MaxQuantity',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]