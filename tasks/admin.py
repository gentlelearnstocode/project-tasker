from django.contrib import admin
from .models import User, Worker, Task
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Worker)
# Register your models here.
