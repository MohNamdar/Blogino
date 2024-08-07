from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('phone', 'bio', 'profile')}),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'created', 'active']
    list_editable = ['active']
    list_filter = ['name', 'article', ('created', JDateFieldListFilter)]
    search_fields = ['article', 'message']
    raw_id_fields = ['article']
