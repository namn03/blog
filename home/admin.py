from django.contrib import admin

from home.models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(LargeCategory)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['category', 'tags']

# Register your models here.
