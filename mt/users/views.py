from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tables_list")  # Убедитесь, что 'tables_list' существует
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def users_list_create(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect('users_list')  # Перенаправление на список пользователей после создания
    users = User.objects.all()
    return render(request, 'users_list.html', {"users": users})

def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'user_detail.html', {"user": user})
