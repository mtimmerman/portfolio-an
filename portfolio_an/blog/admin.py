from portfolio_an.blog.models import Post, Comment, PostAdmin, CommentAdmin
from django.contrib import admin

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
