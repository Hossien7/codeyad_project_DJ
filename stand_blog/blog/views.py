from django.shortcuts import render, get_object_or_404
from blog.models import Article


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    recent_post = Article.objects.all().order_by('-created')[:3]
    return render(request, 'blog/article-details.html', {'article': article})

def show_posts(request):
    articles = Article.objects.all().order_by('-created')
    return render(request, 'blog/articles_list.html', context={'articles': articles})


