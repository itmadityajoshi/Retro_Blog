from django.contrib import admin
from . models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')

admin.site.register(Category,CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'author')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Blog, BlogAdmin)