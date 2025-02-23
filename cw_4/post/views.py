from django.shortcuts import render, redirect
from .models import Post, Thread
from .forms import PostForm, ThreadForm

def index_thread(request):
    if request.method == 'GET':
        form = ThreadForm()
        threads = Thread.objects.all()
        return render(request, 'post/index.html',
                      {
                        'form': form,
                        'threads': threads
                      })
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
def update_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if request.method == "GET":
        form = ThreadForm(instance=thread)
        return render(request, 'post/update_thread.html',
                      {
                        'form': form,
                        'thread': thread
                      })
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
        return redirect('/')

def delete_thread(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
        thread.delete()
        return redirect('/')
    except Thread.DoesNotExist as e:
        return redirect('index')

def thread_details(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if request.method == 'GET':
        form = PostForm()
        posts = Post.objects.filter(thread=thread_id)
        return render(request, 'post/thread_details.html',
                        {
                            'posts': posts,
                            'thread': thread,
                            'form': form
                        })
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            author = form.cleaned_data.get('author')
            picture = form.cleaned_data.get('picture')
            post = Post(
                title=title,
                description=description,
                author=author,
                thread=Thread.objects.get(id=thread_id),
            )
            post.picture.save(picture.name, picture)
            post.save()
        return redirect('thread_details', thread_id)
    
def update_post(request, thread_id, post_id):
    thread = Thread.objects.get(id=thread_id)
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'post/update_post.html',
                        {
                            'post': post,
                            'thread': thread,
                            'form': form
                        })
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('thread_details', thread_id)
        
def delete_post(request, thread_id, post_id):
    try:
        post=Post.objects.get(id=post_id)
        post.delete()
        return redirect('thread_details', thread_id)
    except Post.DoesNotExist as e:
        return redirect('index')