from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('podcast-list/', views.podcast_list, name='podcast_list'),
    path('podcast/<slug>', views.podcast_single, name='podcast_single'),
    path('about/', views.about, name='about'),
    path('article-list/', views.article_list, name='article_all'),
    path('article-list/<str:cat>', views.article_list, name='article_list'),
    path('tag/<str:tag>', views.tag_list, name='tag_list'),
    path('article/<slug>', views.article_single, name='article_single'),
]
