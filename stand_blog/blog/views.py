from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator


def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/article-details.html', {'article': article})

def show_posts(request):
    article = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', context={'articles': object_list})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    article = category.article_set.all()    # Reverse access in db category to article
    
    return render(request, 'blog/articles_list.html', {'articles': article})
