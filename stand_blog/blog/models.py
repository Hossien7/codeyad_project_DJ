from django.db import models
from django.contrib.auth import User

# Many to Many
# Many to one ==> ForeignKey
# One to One

""" Each article has a user and each user can has several article ==>ManyToOne"""
class Article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=750)
    body = models.TextField()
    image = models.ImageField(upload_to='Images/ArticlesImage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
