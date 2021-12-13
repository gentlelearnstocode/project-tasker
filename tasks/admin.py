from django.contrib import admin
from .models import User, Worker, Task, UserProfile
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(UserProfile)
# Register your models here.
