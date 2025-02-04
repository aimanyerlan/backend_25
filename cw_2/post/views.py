from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CreatePostForm

# Create your views here.
def index(request):
    if request.method == "GET":
        form = CreatePostForm()
        posts = Post.objects.all()
        return render(request, 'post/index.html',
                      {
                          'posts': posts,
                          'form': form
                      })
def post_create(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = CreatePostForm()
    return render(request, 'post/post_form.html', {'form': form})


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_details.html', {'post': post})

def post_delete(request, id):
    try:
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect('/posts/')
    except Post.DoesNotExist as e:
        form = CreatePostForm()
        posts = Post.objects.all()
        return render(request, 'post/index.html',
                      {'posts': posts,
                       'form': form,
                       'error': "Couldn't delete post since it does not exist"
                       })
        