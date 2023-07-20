from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True,null=True,max_length=100000)
    author = models.CharField(max_length=1000,blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField()
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:post", kwargs={
            'slug':self.slug
        })