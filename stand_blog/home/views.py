from django.shortcuts import render
from blog.models import Article

def home(request):
    obj = Article.objects.all()
    return render(request, 'home/index.html', {'articles': obj})