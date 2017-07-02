from django.contrib import admin

from home.models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(LargeCategory)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    exclude = ('comments',)

# Register your models here.
