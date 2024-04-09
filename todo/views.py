from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag
from todo.forms import TagCreateForm, TaskCreateForm


class IndexView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag
    ordering = ["name"]
    paginate_by = 5


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todo:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:index")


class TaskCompleteView(generic.View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.completed = not task.completed
        task.save()
        return redirect(request.META.get('HTTP_REFERER'))
