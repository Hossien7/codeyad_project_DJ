from django.shortcuts import render
from blog.models import Article, New


def home(request):
    obj = Article.objects.all().filter(status=True)
    obj1 = New.objects.get(id=1)
    obj1.title = 'Farid rezaii'
    obj1.save()
    return render(request, 'home/index.html', {'articles': obj})


