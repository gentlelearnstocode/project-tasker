from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from tasks.forms import CustomUserCreationForm, TaskModelForm
from .models import Task, Worker
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/task_list.html'
    queryset = Task.objects.all()
    context_object_name = 'tasks'

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    queryset = Task.objects.all()
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskModelForm
    context_object_name = 'task'
    def get_success_url(self):
        return reverse("tasks:task-list")

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    queryset = Task.objects.all()
    form_class = TaskModelForm
    context_object_name = 'task'
    def get_success_url(self):
        return reverse("tasks:task-list")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    queryset = Task.objects.all()
    def get_success_url(self):
        return reverse("tasks:task-list")
    
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')  



# def tasks_list(request):
#     tasks = Task.objects.all()
#     context = {
#         'tasks' : tasks
#     }
#     return render(request, 'tasks/tasks_list.html', context)


# #---------------------------------------------
# def task_detail(request, pk):   
#     task = Task.objects.get(id=pk)
#     context = {
#         'task' : task
#     }
#     return render(request, 'tasks/task_detail.html', context)

# def task_create(request):
#     form = TaskModelForm()
#     if request.method == 'POST':
#         print('Receiving a post request')
#         form = TaskModelForm (request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/tasks')

#     context = {
#         'form' : form
#     }
#     return render(request, 'tasks/task_create.html', context)

# def task_update(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskModelForm(instance=task)
#     if request.method == 'POST':
#         form = TaskModelForm (request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('/tasks')
#     context = {
#         'form': form,
#         'task': task
#     }
#     return render(request, 'tasks/task_update.html', context)

# def task_delete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return redirect('/tasks')

# def home_page(request):
#     return render(request, 'home.html')