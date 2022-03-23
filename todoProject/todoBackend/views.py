from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path, reverse

from .models import TodoList
from .forms.taskForm import AddTask

# Create your views here.
def index(request):
    taskList = TodoList.objects.all()
        
    if request.method=='POST':
        form = AddTask(request.POST)

        if form.is_valid():
            # print(form.data)
            TodoList.objects.create(**form.cleaned_data)
            TodoList.save()


            return HttpResponseRedirect('/todoBackend/')

    else:
        form = AddTask()

    return render(request, 'tasks/index.html', {"taskList":taskList, "form": form} )


def detail(request, TodoList_id):
    task = get_object_or_404(TodoList, pk=TodoList_id)

    return render(request, 'tasks/detail.html', {'task':task})


def edit(request, TodoList_id):
    task = get_object_or_404(TodoList, pk=TodoList_id)
    
    if request.method == 'POST':
        form = AddTask(request.POST)

        if form.is_valid():
            # print(form.data['task_description'])

            task.name = form.data['task_name']
            task.description = form.data['task_description']

            task.save()

            return HttpResponseRedirect('/todoBackend/%s' %(TodoList_id))

    else:
        form = AddTask()
    
    return render(request, 'tasks/detail.html', {"task":task, "form":form })
    


