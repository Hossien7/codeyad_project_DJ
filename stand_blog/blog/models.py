from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
# Many to Many
# Many to one ==> ForeignKey
# One to One
# set null
# set default
# cascade
# protect


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
class ArticleManager(models.Manager):
    # def counter(self):
    #     return len(self.all())
    
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)
    
    def published(self):
        return self.filter(status=True)
    
    
""" Each article has a user and each user can has several article ==>ManyToOne"""




class Article(models.Model):
    CHOICES = (
        ('A', 'ais'),
        ('B', 'blue'),
    )
    # Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) If you use SET_NULL you must do null=True
    # Author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='1') If you use SET_DEFAULT you must do default
    
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=750, choices=CHOICES, default='A', unique_for_date='up_date')
    category = models.ManyToManyField(Category, related_name='category') # ==> we can change 'category' to '+' for reverse access disabling 
    body = models.TextField()
    image = models.ImageField(upload_to='Images/ArticlesImage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    up_date = models.DateField(timezone.now())
    status = models.BooleanField(default=False)
    objects = models.Manager()  # it must be here if you do custom manager
    custom_object = ArticleManager()
    slug = models.SlugField(null=True, unique=True, blank=True) # Slug Field for using in URLS
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created',)


    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})  # changed for slug
    
    def save(self, force_insert = False, force_update = False, update_fields = None, using = None):
        self.slug = slugify(self.title)
        return super(Article, self).save()

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'

    


class New(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()


    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ', '_')
        super(New, self).save(args, kwargs)


# null ==> in DB
# blank ==> in form
# help_text ==> 
# unique ==>
# dbcolumn ==> customize title
# editable
# choices
# unique_for_date='up_date'


# CRUD CREATE   READ                        UPDATE    DELETE
#      .save     .filter(status=True) .create()    .get() .save               .delete()
# new = New.objects.get(id=1)   reading with id == 1    get() just returned 1 object 
# Queryset: a set of collections... like .all()  .filter()   lazy evaluation... is slower than.... db not hit