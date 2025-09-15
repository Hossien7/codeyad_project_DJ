from blog.models import Article


def recent_post(request):
    recent_posts = Article.objects.order_by('-created')[:3]
    return {'recent_article': recent_posts}