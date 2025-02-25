from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import Post, Thread
from .forms import PostForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("posts_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {"posts": posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "my_posts.html", {"posts": posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    is_author = post.author == request.user
    is_superuser = request.user.is_superuser
    return render(request, "post_detail.html", {"post": post, "is_author": is_author, "is_superuser": is_superuser})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user  
            post.save()  
            return redirect("posts_list") 
    else:
        form = PostForm()
    
    return render(request, "post_form.html", {"form": form})

@login_required
@permission_required("posts.change_post", raise_exception=True)
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to edit this post")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "post_form.html", {"form": form, "post": post})

@login_required
@permission_required("posts.delete_post", raise_exception=True)
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect("posts_list")
    return HttpResponseForbidden("You are not allowed to delete this post")
