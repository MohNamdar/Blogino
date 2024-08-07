from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('page/', views.page, name='page'),
    path('podcast-list/', views.podcast_list, name='podcast_list'),
    path('podcast/', views.podcast_single, name='podcast_single'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('article-list/<str:cat>', views.article_list, name='article_list'),
    path('article/<slug>', views.article_single, name='article_single'),
    path('faq/', views.faq, name='faq'),
]
