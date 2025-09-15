from django.urls import path

from blog.views import post_detail, show_posts


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', post_detail, name='post_detail'),  
    path('list/', show_posts, name='show_posts') 

]
