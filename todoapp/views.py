from django.shortcuts import render, redirect

from .models import Vazifa
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks=Vazifa.objects.all()

    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks,'form':form}
    return render(request,'todoapp/list.html',context)

def updateTask(request,pk):
    task=Vazifa.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request,'todoapp/update_task.html',context)

def  deleteTask(request,pk):
    item=Vazifa.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, 'todoapp/delete.html',context)