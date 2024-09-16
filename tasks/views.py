from django.shortcuts import render
from .models import Task
from datetime import date

def index(request):
    """ 
    A view to display all the saved tasks, with the tasks due soonest at the top.
    """
    to_do_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')

    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks,
        'today': date.today(),
    }

    return render(request, 'index.html', context)