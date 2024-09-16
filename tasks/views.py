from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import date
from .forms import TaskForm

def index(request):
    """ 
    A view to display all the saved tasks,
    with the tasks due soonest at the top.
    View also displays a form to add a new task.
    """
    to_do_tasks = Task.objects.filter(
        completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(
        completed=True).order_by('due_date')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = TaskForm()

    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks,
        'today': date.today(),
        'form': form,
    }

    return render(request, 'index.html', context)


def toggle_done(request, task_id):
    """
    A view to toggle the completed status of a task.
    """
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    """
    A view to delete a task.
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')