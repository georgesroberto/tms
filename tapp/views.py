from typing import Any
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

# Logic
class TaskList(ListView):
    model = Task

    def get(self, request):
        tasks = Task.objects.all().order_by('due_date')
        paginator = Paginator(tasks, 4, 1, allow_empty_first_page=True)
        page = request.GET.get('page')

        try:
            paginated_tasks = paginator.page(page)
        except PageNotAnInteger:
            paginated_tasks = paginator.page(1)
        except EmptyPage:
            paginated_tasks = paginator.page(paginator.num_pages)


        context = {
            'tasks': paginated_tasks,
            'title': 'Task List'
        }

        return render(request, 'tapp/index.html', context)


class TaskDetail(DetailView):
    model = Task
    template_name = 'tapp/detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Task Detail'
        context['tags'] = Task.get_tag_name(self)
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form = TaskForm
    fields = ['title', 'description', 'status', 'due_date', 'author', 'tag']
    success_url = '/'
    template_name = 'tapp/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Create'
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form = TaskForm
    fields = ['title', 'description', 'status', 'due_date', 'avator', 'author', 'tag']
    success_url = '/'
    template_name = 'tapp/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Update'
        return context

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tapp/delete.html'
    context_object_name = 'task'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Delete'
        return context

