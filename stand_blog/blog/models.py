from django.db import models
from django.contrib.auth import User
from django.utils import timezone
# Many to Many
# Many to one ==> ForeignKey
# One to One
# set null
# set default
# cascade
# protect


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    
""" Each article has a user and each user can has several article ==>ManyToOne"""
class Article(models.Model):
    CHOICES = (
        ('A', 'ais')
        ('B', 'blue')
    )
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) If you use SET_NULL you must do null=True
    # Author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='1') If you use SET_DEFAULT you must do default
    title = models.CharField(max_length=750, choices=CHOICES, default='A', unique_for_date='up_date')
    category = models.ManyToManyField
    body = models.TextField()
    image = models.ImageField(upload_to='Images/ArticlesImage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    up_date = models.DateField(timezone.now())
    
    def __str__(self):
        return f'{self.title} - {self.body[:30]}'





# null ==> in DB
# blank ==> in form
# help_text ==> 
# unique ==>
# dbcolumn ==> customize title
# editable
# choices
# unique_for_date='up_date'