# Generated by Django 5.0.7 on 2024-09-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0003_alter_task_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='avator',
            field=models.ImageField(blank=True, upload_to='profiles/'),
        ),
    ]
