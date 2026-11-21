from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect

from tasks.forms import TagForm, TaskForm
from tasks.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse(
            "tasks:task-list",
        )


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse(
            "tasks:task-list",
        )


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


@require_POST
def task_toggle(request, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])

    return redirect("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse(
            "tasks:tag-list",
        )


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse(
            "tasks:tag-list",
        )


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
