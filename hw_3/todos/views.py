from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import CreateTodoForm

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == "POST":
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('index')      
    else:
        form = CreateTodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('index')

def todo_new_status(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.status = not todo.status
    todo.save()
    return redirect('index')
