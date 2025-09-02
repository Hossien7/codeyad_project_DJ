from django.shortcuts import render, get_object_or_404
from blog.models import Article


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article-details.html', {'article': article})
