from django.contrib import admin
from .models import Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author')


admin.site.register(Post, AuthorAdmin)