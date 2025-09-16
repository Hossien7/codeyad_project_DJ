from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    recent_post = Article.objects.all().order_by('-created')[:3]
    return render(request, 'blog/article-details.html', {'article': article})

def show_posts(request):
    articles = Article.objects.all().order_by('-created')
    return render(request, 'blog/articles_list.html', context={'articles': articles})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    article = category.article_set.all()    # Reverse access in db category to article
    return render(request, 'blog/articles_list.html', {'articles': article})
