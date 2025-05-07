from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def create(request):
    todo = Todo()
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    todo.is_completed = False
    
    todo.save()

    context = {
        'todo' : todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()
    return redirect('todos:index')