# Generated by Django 3.0.5 on 2021-12-29 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_coursewisestudent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursewisestudent',
            old_name='Student',
            new_name='student',
        )
    ]
