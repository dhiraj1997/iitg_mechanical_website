# Generated by Django 2.2.1 on 2019-07-19 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0058_auto_20190719_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursepage',
            name='course_type',
        ),
        migrations.RemoveField(
            model_name='coursepage',
            name='eligible_programmes',
        ),
        migrations.RemoveField(
            model_name='coursepage',
            name='eligible_specializations',
        ),
        migrations.DeleteModel(
            name='CourseProgrammes',
        ),
        migrations.DeleteModel(
            name='CourseSpecializations',
        ),
        migrations.DeleteModel(
            name='CourseTypes',
        ),
    ]