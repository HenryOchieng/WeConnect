from django.contrib import admin
from Blog.models import Post, Comment, Preference

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Preference)
