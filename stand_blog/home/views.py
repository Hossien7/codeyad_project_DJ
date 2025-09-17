from django.shortcuts import render
from blog.models import Article


def home(request):
    # obj = Article.objects.all().filter(status=True)
    # obj = Article.objects.published()
    obj = Article.custom_object.all()
    recent_post = Article.objects.all().order_by('-created')[:3]
    # obj1 = New.objects.get(id=1)
    # obj1.title = 'Farid rezaii'
    # obj1.save()
    return render(request, 'home/index.html', {'articles': obj, 'recent_posts': recent_post})


