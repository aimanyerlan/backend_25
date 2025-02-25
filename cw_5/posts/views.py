# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.context_processors import auth
# from django.shortcuts import render, redirect
# from .models import Post, Thread
# from .forms import PostForm, ThreadForm
# from django.contrib.auth.decorators import login_required, permission_required


# def index_thread(request):
#     if request.method == 'GET':
#         form = ThreadForm()
#         threads = Thread.objects.all()
#         return render(request, 'post/index.html',
#                       {
#                         'form': form,
#                         'threads': threads
#                       })
    
#     if request.method == "POST":
#         form = ThreadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
# @login_required 
# @permission_required('posts.change_thread')      
# def update_thread(request, thread_id):
#     thread = Thread.objects.get(id=thread_id)
#     if request.method == "GET":
#         form = ThreadForm(instance=thread)
#         return render(request, 'post/update_thread.html',
#                       {
#                         'form': form,
#                         'thread': thread
#                       })
#     if request.method == 'POST':
#         form = ThreadForm(request.POST, instance=thread)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
    
# @login_required
# @permission_required('posts.delete_thread')
# def delete_thread(request, thread_id):
#     try:
#         thread = Thread.objects.get(id=thread_id)
#         thread.delete()
#         return redirect('/')
#     except Thread.DoesNotExist as e:
#         return redirect('index')


# def thread_details(request, thread_id):
#     thread = Thread.objects.get(id=thread_id)
#     if request.method == 'GET':
#         form = PostForm()
#         posts = Post.objects.filter(thread=thread_id)
#         return render(request, 'post/thread_details.html',
#                         {
#                             'posts': posts,
#                             'thread': thread,
#                             'form': form
#                         })
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             description = form.cleaned_data.get('description')
#             author = form.cleaned_data.get('author')
#             picture = form.cleaned_data.get('picture')
#             post = Post(
#                 title=title,
#                 description=description,
#                 author=author,
#                 thread=Thread.objects.get(id=thread_id),
#             )
#             post.picture.save(picture.name, picture)
#             post.save()
#         return redirect('thread_details', thread_id)
    
# @login_required   
# @permission_required('posts.change_post')
# def update_post(request, thread_id, post_id):
#     thread = Thread.objects.get(id=thread_id)
#     post = Post.objects.get(id=post_id)
#     if request.method == "GET":
#         form = PostForm(instance=post)
#         return render(request, 'post/update_post.html',
#                         {
#                             'post': post,
#                             'thread': thread,
#                             'form': form
#                         })
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#         return redirect('thread_details', thread_id)
    
# @login_required    
# @permission_required('posts.delete_post')    
# def delete_post(request, thread_id, post_id):
#     try:
#         post=Post.objects.get(id=post_id)
#         post.delete()
#         return redirect('thread_details', thread_id)
#     except Post.DoesNotExist as e:
#         return redirect('index')

# @login_required 
# def log_in(request):
#     if request.method == "POST":
#         redirect_url = request.GET.get('next', '/')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(redirect_url)
#         return render(request, 'auth/login.html')
    
# @login_required
# def log_out(request):
#     logout(request)
#     return redirect('index')

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
        form = PostForm(request.POST, request.FILES)  # Не забываем request.FILES!
        if form.is_valid():
            post = form.save(commit=False)  # Создаем объект, но не сохраняем
            post.author = request.user  # Привязываем текущего пользователя
            post.save()  # Сохраняем в базе
            return redirect("posts_list")  # Перенаправляем после успешного создания
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
