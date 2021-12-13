from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
# Create your models here.

class User(AbstractUser):
    is_supervisor = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

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
        ('Church', 'Church'),
        ('Other', 'Other'),
        )

    Task_CHOICES = (
        ('Assistant', 'Assistant'),
        ('Cleaning', 'Cleaning'),
        ('Church Service', 'Church Service'),
        ('Monitor', 'Monitor'),
        ('Tutoring', 'Tutoring'),
        ('Supervising', 'Supervising'),
        ('Other', 'Other'),
    )
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    on_date = models.DateField(null=True)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=100)
    task = models.CharField(choices=Task_CHOICES, max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    worker = models.ForeignKey('Worker', null=True, blank=True, on_delete=models.SET_NULL)
    #functions
    def __str__(self):
        return f'{self.title} {self.date_added}'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    department = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

def user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance) 

post_save.connect(user_created, sender=User)