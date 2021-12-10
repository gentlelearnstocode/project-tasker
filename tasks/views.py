from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from tasks.forms import TaskModelForm
from .models import Task, Worker

# Create your views here.

def tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


#---------------------------------------------
def task_detail(request, pk):   
    task = Task.objects.get(id=pk)
    context = {
        'task' : task
    }
    return render(request, 'tasks/task_detail.html', context)

def task_create(request):
    form = TaskModelForm()
    if request.method == 'POST':
        print('Receiving a post request')
        form = TaskModelForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks')

    context = {
        'form' : form
    }
    return render(request, 'tasks/task_create.html', context)

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskModelForm(instance=task)
    if request.method == 'POST':
        form = TaskModelForm (request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks')
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'tasks/task_update.html', context)

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/tasks')