# Generated by Django 3.0.5 on 2021-12-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_course_exam_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='exam_cwt',
            field=models.CharField(default=0, max_length=50),
        ),
    ]