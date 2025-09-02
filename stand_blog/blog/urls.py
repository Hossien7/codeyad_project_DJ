from django.urls import path

from blog.views import post_detail


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', post_detail, name='post_detail'),   

]
