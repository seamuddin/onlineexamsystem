# Generated by Django 3.0.5 on 2021-12-29 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_course_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='exam_cwt',
            new_name='exam_course',
        ),
    ]