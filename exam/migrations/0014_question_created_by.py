# Generated by Django 3.0.5 on 2021-12-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20211229_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_by',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
