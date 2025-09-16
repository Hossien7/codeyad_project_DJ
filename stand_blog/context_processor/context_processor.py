from blog.models import Article, Category


def recent_post(request):
    recent_posts = Article.objects.order_by('-created')[:3]
    return {'recent_article': recent_posts}

def show_categories(request):
    recent_category = Category.objects.all()[:3]
    return {'category': recent_category}