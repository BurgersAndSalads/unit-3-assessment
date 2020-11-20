from django.shortcuts import render, redirect
from .models import Task
from django.forms import ModelForm

# Create your views here.


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'home.html', {
        'task_list': tasks,
        'form': form,
    })

def add(request):
    form = TaskForm(request.POST)
    if form.is_valid:
        new_task = form.save(commit=False)
        new_task.save()
    return redirect('/')


def delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')
