from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Comment
from django.core.paginator import Paginator
from .form import ContactUsForm

def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        reply_instance = None
        if parent_id:
            try:
                reply_instance = Comment.objects.get(id=parent_id)
            except Comment.DoesNotExist:
                reply_instance = None
        Comment.objects.create(article=article, body=body, user=request.user, reply=reply_instance)
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

def search(request):
    q = request.GET.get('q')    # the name of search_input in form
    article = Article.objects.filter(title__icontains=q)
    print(article)
    page_number = request.GET.get('page')
    paginator = Paginator(article, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', context={'articles': object_list})

def contact_us(request):  
    if request.method == 'POST':
        form = ContactUsForm(request.POST or None)  #
        if form.is_valid():
            
            print(form.cleaned_data['name']) 
            return redirect('main:home_page')
        
    form = ContactUsForm(request.POST or None)
    return render(request, 'blog/contact_us.html', context={'form': form})