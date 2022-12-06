from django.contrib import admin
from .models import Post, TopPost, LatestPost

# admin.site.register(Post)
# admin.site.register(TopPost)
# admin.site.register(LatestPost)

@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('header',)
    list_display = ('header', 'name', 'date')

@admin.register(TopPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', "count",)

@admin.register(LatestPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date')