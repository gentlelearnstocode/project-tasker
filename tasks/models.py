from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.

class User(AbstractUser):
    pass

class Task(models.Model):
    LOCATION_CHOICES = (
        ('Elizah Hall', 'Elizah Hall'),
        ('Solomon Hall', 'Solomon Hall'),
        ('Eve Hall', 'Eve Hall'),
        ('Sarah Hall', 'Sarah Hall'),
        ('Esther Hall', 'Esther Hall'),
        ('Ruth Hall', 'Ruth Hall'),
        ('Guest House', 'Guest House'),
        ('Library', 'Library'),
        ('Cafeteria', 'Cafeteria'),
        ('IT Building', 'IT Building'),
        ('Admin Building', 'Admin Building'),
        ('Science Building', 'Science Building'),
        ('Hope Channel', 'Hope Channel'),
        ('Church', 'Church')
        )

    CATEGORY_CHOICES = (
        ('Assistant', 'Assistant'),
        ('Monitor', 'Monitor'),
        ('Janitor', 'Janitor'),
        ('Supervisor', 'Supervisor'),
        ('Video Editor', 'Video Editor'),
        ('Chaplain', 'Chaplain')
    )
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    on_date = models.DateField(null=True)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    description = models.TextField(null=True, blank=True)
    worker = models.ForeignKey('Worker', on_delete=CASCADE)
    #functions
    def __str__(self):
        return f'{self.title} {self.date_added}'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    job_title = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.user.username