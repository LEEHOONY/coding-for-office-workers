from django.contrib import admin
from .models import Article, comment

# Register your models here.
@admin.register(Article, comment)
class BlogAdmin(admin.ModelAdmin):
    pass
