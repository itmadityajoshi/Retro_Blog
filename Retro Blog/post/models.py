from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICE =(
    ('draft', 'Draft'),
    ('published', 'Published')
)

class Blog(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True)  #slug is a part of url that identifies the particular part of website
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_descriptions = models.CharField(max_length=2000)
    blog_body = models.CharField(max_length=5000)
    status = models.CharField(choices= STATUS_CHOICE, default='draft', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

