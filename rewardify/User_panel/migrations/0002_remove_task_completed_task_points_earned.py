# Generated by Django 5.0.6 on 2024-09-02 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='points_earned',
            field=models.IntegerField(default=0),
        ),
    ]
