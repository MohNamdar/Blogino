from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.models import *


# Create your views here.


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)


def gallery(request):
    return render(request, 'blog/gallery.html')


def page(request):
    return render(request, 'blog/page.html')


def podcast_single(request):
    return render(request, 'blog/podcast_single.html')


def podcast_list(request):
    return render(request, 'blog/podcast_list.html')


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


def article_single(request, slug):
    article = Article.objects.get(slug=slug)
    comments = article.comments.filter(active=True)
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'blog/article_single.html', context)


CATEGORY_MAP = {
    'هوش مصنوعی': 'AI',
    'تکنولوژی': 'TCH',
    'برنامه نویسی': 'PRG',
    'امنیت': 'SEC',
    'پادکست': 'PDC',
    'ویدئوکست': 'VDC',
}


def article_list(request, cat=''):
    if cat:
        category_value = CATEGORY_MAP.get(cat)

        if category_value:
            articles = Article.objects.filter(category=category_value)
        else:
            return redirect('blog:home')
    else:
        articles = Article.objects.all()

    context = {
        'category': cat,
        'articles': articles
    }

    return render(request, 'blog/article_list.html', context)


def faq(request):
    return render(request, 'blog/faq.html')
