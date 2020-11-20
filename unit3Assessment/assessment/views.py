from django.shortcuts import render, redirect
from .models import Task
from django.forms import ModelForm
from django.db.models import Sum

# Create your views here.


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    total = Task.objects.all().aggregate(Sum('time'))
    return render(request, 'home.html', {
        'task_list': tasks,
        'form': form,
        'total': total,
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