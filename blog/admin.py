from django.contrib import admin
from .models import Article, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'profile')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('phone', 'bio', 'profile')}),
    )
