from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.forms import *
from blog.models import *
import requests
from datetime import datetime


# Create your views here.


def home(request):
    articles = Article.objects.all()
    today = datetime.today()
    url = f'https://holidayapi.ir/gregorian/{today.year}/{today.month}/{today.day}'
    response = requests.get(url)
    data = response.json()
    events = []
    for event in data['events']:
        events.append(event['description'])

    context = {
        'articles': articles,
        'events': events
    }

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
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    form = CommentForm()
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
        'comment': comment
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
