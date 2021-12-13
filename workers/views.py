from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.views import Worker
from django.urls import reverse
from .forms import WorkerModelForm
# Create your views here.



class WorkerListView(LoginRequiredMixin, generic.ListView):
    template_name = 'workers/worker_list.html'

    def get_queryset(self):
        return Worker.objects.all()


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'workers/worker_create.html'
    form_class = WorkerModelForm
    
    def get_success_url(self):
        return reverse('workers:worker-list')

    def form_valid(self, form):
        worker = form.save(commit=False)
        worker.organization = self.request.user.userprofile
        worker.save()
        return super(WorkerCreateView, self).form_valid(form)

class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'workers/worker_detail.html'
    context_object_name = 'worker'
    def get_queryset(self):
        return Worker.objects.all()

# class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
#     template_name =

# class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
#     template_name =

class WorkerListView(LoginRequiredMixin, generic.ListView):
    template_name = 'workers/worker_list.html'
    context_object_name = 'worker'
    def get_queryset(self):
        return Worker.objects.all()

class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'workers/worker_update.html'
    form_class = WorkerModelForm
    
    def get_success_url(self):
        return reverse('workers:worker-list')

    def get_queryset(self):
        return Worker.objects.all()

class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'workers/worker_delete.html'
    context_object_name = 'worker'

    def get_queryset(self):
        return Worker.objects.all()

    def get_success_url(self):
        return reverse('workers:worker-list')