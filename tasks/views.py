from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *

from .forms import *

# Create your views here.

def index(request):

    # return HttpResponse("Hi there my list is comming!")
    tasks = Task.objects.all()
    form =TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.completed = False
        if form.is_valid():
            form.save()
            return redirect('/todo/')
        else:
            print(f'form not valied {form.errors}')
    print([t.completed for t in tasks])
    context = {'tasks':tasks, 'title':'Main page', 'form':form}

    return render(request, 'tasks/todo_list.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST' and task:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    context = {'form': form, 't_id': task.id , 'title':'Update task'}
    return render(request,'tasks/update_task.html', context)


def delete(request, pk):

    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/todo/')
    
    context = {'task':task}

    return render(request, 'tasks/confirm_delete.html', context)

    pass