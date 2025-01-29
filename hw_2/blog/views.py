from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form})
