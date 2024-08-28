from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('podcasts/', views.podcast_list, name='podcast_list'),
    path('podcast/<slug>', views.podcast_single, name='podcast_single'),
    path('resume/', views.about, name='about'),
    path('articles/', views.article_list, name='article_all'),
    path('articles/<str:cat>', views.article_list, name='article_list'),
    path('tag/<str:tag>', views.tag_list, name='tag_list'),
    path('article/<slug>', views.article_single, name='article_single'),
    path('search/', views.search, name='search'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', views.log_out, name='logout'),
]
