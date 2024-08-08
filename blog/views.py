from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import *
from blog.models import *
import requests
from datetime import datetime

PAGINATION_PER_PAGE = 5
CATEGORY_MAP = {
    'هوش مصنوعی': 'AI',
    'تکنولوژی': 'TCH',
    'برنامه نویسی': 'PRG',
    'امنیت': 'SEC',
    'روزانه': 'DAY'
}


# Create your views here.
def home(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, PAGINATION_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        raise PageNotAnInteger
    except EmptyPage:
        raise EmptyPage

    today = datetime.today()
    url = f'https://holidayapi.ir/gregorian/{today.year}/{today.month}/{today.day}'
    response = requests.get(url)
    data = response.json()
    events = []
    for event in data['events']:
        events.append(event['description'])

    context = {
        'page_obj': page_obj,
        'events': events,
    }

    return render(request, 'blog/home.html', context)


def gallery(request):
    return render(request, 'blog/gallery.html')


def podcast_single(request):
    return render(request, 'blog/podcast_single.html')


def podcast_list(request, cat=''):
    if cat:
        category_value = CATEGORY_MAP.get(cat)

        if category_value:
            podcasts = Podcast.objects.filter(category=category_value)
        else:
            return redirect('blog:home')
    else:
        podcasts = Podcast.objects.all()
        cat = 'همه پادکست ها'

    paginator = Paginator(podcasts, PAGINATION_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        raise PageNotAnInteger
    except EmptyPage:
        raise EmptyPage

    context = {
        'page_obj': page_obj,
        'category': cat,
    }

    return render(request, 'blog/podcast_list.html', context)


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


def article_list(request, cat=''):
    if cat:
        category_value = CATEGORY_MAP.get(cat)

        if category_value:
            articles = Article.objects.filter(category=category_value)
        else:
            return redirect('blog:home')
    else:
        articles = Article.objects.all()

    paginator = Paginator(articles, PAGINATION_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        raise PageNotAnInteger
    except EmptyPage:
        raise EmptyPage

    context = {
        'page_obj': page_obj,
        'category': cat,
    }

    return render(request, 'blog/article_list.html', context)


def tag_list(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    articles = Article.objects.filter(tags=tag)
    paginator = Paginator(articles, PAGINATION_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        raise PageNotAnInteger
    except EmptyPage:
        raise EmptyPage

    context = {
        'page_obj': page_obj,
        'tag': tag
    }

    return render(request, 'blog/tag_list.html', context)
