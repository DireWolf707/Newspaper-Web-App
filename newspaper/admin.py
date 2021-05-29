from django.contrib import admin
from .models import Article,Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    #fields = ('comment',)
    
    
class ArticleAdmin(admin.ModelAdmin):
    inlines =(CommentInline,)
    readonly_fields = ('created','edited',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)