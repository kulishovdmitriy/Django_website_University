# Generated by Django 4.2 on 2024-08-05 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
    ]
