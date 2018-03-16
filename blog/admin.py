from django.contrib import admin
from .models import Post, Comment, Categories, BlogType


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categories)
admin.site.register(BlogType)