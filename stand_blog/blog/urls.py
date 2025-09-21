from django.urls import path

from blog.views import post_detail, show_posts, category_detail, search, contact_us


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', post_detail, name='post_detail'),  
    path('list/', show_posts, name='show_posts') ,
    path('category/<int:pk>/', category_detail, name='category'),
    path('search/', search, name='search_articles'),
    path('contact_us/',contact_us, name='contact_us')

]
