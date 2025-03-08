from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import TodoForm

def log_in(request):
    if request.method == "POST":
        redirect_url = request.GET.get('next', 'todos_list')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            return render(request, "todos/login.html", {"error": "Invalid credentials"})
    return render(request, "todos/login.html")

@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def todos_list(request):
    user_todos = Todo.objects.filter(user=request.user)
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todos_list')
        
    return render(request, 'todos/todos_list.html', {'todos': user_todos, 'form': form})

@login_required
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)  
    return render(request, "todos/todo_detail.html", {"todo": todo})


@login_required
def todo_new_status(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.status = not todo.status
    todo.save()
    return redirect('todo_detail', todo_id=todo.id)

@login_required
@permission_required('todos.delet_todo', raise_exception=True)
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todos_list')
