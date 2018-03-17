from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField


class Categories(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])

    class Meta:
        verbose_name_plural = 'Categories'


class BlogType(models.Model):
    type_title = models.CharField(max_length=100, default='Default')
    description = models.TextField(max_length=155)

    def __str__(self):
        return self.type_title


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, related_name='categories')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=False, null=True, blank=True)
    text = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(
            blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def publish(self):
        self.published_date = timezone.now()
        self.published = True
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text