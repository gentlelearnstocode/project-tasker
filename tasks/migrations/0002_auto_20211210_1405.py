# Generated by Django 3.1.4 on 2021-12-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='on_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='job_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
