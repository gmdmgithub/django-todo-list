from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *

from .forms import *

# Create your views here.

def index(request):

    # return HttpResponse("Hi there my list is comming!")
    
    print(request)

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
        
    context = {'tasks':tasks, 'title':'Main page', 'form':form}

    return render(request, 'tasks/todo_list.html', context)

def update(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')

    return render(request,'tasks/update_task.html')