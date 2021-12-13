from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.views import Worker
from django.urls import reverse
from .forms import WorkerModelForm
from .mixins import SupervisorAndLoginRequiredMixin
# Create your views here.

class WorkerCreateView(SupervisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'workers/worker_create.html'
    form_class = WorkerModelForm
    
    def get_success_url(self):
        return reverse('workers:worker-list')

    def form_valid(self, form):
        worker = form.save(commit=False)
        worker.department = self.request.user.userprofile
        worker.save()
        return super(WorkerCreateView, self).form_valid(form)

class WorkerDetailView(SupervisorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'workers/worker_detail.html'
    context_object_name = 'worker'
    def get_queryset(self):
        department = self.request.user.userprofile
        return Worker.objects.filter(department=department)

# class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
#     template_name =

# class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name =

class WorkerListView(SupervisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'workers/worker_list.html'
    context_object_name = 'worker'
    def get_queryset(self):
        department = self.request.user.userprofile
        return Worker.objects.filter(department=department)

class WorkerUpdateView(SupervisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'workers/worker_update.html'
    form_class = WorkerModelForm
    
    def get_success_url(self):
        return reverse('workers:worker-list')

    def get_queryset(self):
        return Worker.objects.all()

class WorkerDeleteView(SupervisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'workers/worker_delete.html'
    context_object_name = 'worker'

    def get_queryset(self):
        department = self.request.user.userprofile
        return Worker.objects.filter(department=department)

    def get_success_url(self):
        return reverse('workers:worker-list')