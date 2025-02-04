from django.shortcuts import render
from .models import Article

def index(request):
    if request.method == "GET":
        articles = Article.objects.all
        context = {'articles': articles}
        return render(request, "blog/index.html", context)
    
def article(request, article_id):
    if request.method == "GET":
        a = Article.objects.get(pk=article_id)
        context = {'my_article': a}
        return render(request, "blog/article.html", context)
    