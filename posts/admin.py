from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title',)


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)


