# Generated by Django 5.1 on 2024-08-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='classrooms',
            field=models.ManyToManyField(related_name='groups', to='groups.classroom'),
        ),
    ]
