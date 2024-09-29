from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.contrib.postgres.search import TrigramSimilarity
from blog.forms import *
from blog.models import *
import requests
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

PAGINATION_PER_PAGE = 6
CATEGORY_MAP = {
    'هوش مصنوعی': 'AI',
    'تکنولوژی': 'TCH',
    'برنامه نویسی': 'PRG',
    'امنیت': 'SEC',
    'روزانه': 'DAY'
}


# Create your views here.
def home(request):
    today = datetime.today()
    url = f'https://holidayapi.ir/gregorian/{today.year}/{today.month}/{today.day}'
    response = requests.get(url)
    data = response.json()
    events = []
    for event in data['events']:
        events.append(event['description'])

    context = {
        'events': events,
    }

    return render(request, 'blog/home.html', context)


class GalleryListView(ListView):
    model = Image
    paginate_by = 10
    template_name = "blog/gallery.html"


def podcast_single(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    comments = podcast.comments.filter(active=True)
    form = CommentForm()
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.podcast = podcast
            comment.save()
    context = {
        'podcast': podcast,
        'comments': comments,
        'form': form,
        'comment': comment
    }
    return render(request, 'blog/podcast_single.html', context)


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
        cat = 'همه مقاله‌ها'

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


def search(request):
    query = None
    result = []

    if 'query' in request.GET:
        query = request.GET['query']
        result = (Article.objects.annotate(similarity=TrigramSimilarity('title', query))
                  .filter(similarity__gte=0.1).order_by('-similarity'))

    paginator = Paginator(result, PAGINATION_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        raise PageNotAnInteger
    except EmptyPage:
        raise EmptyPage

    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'blog/article_list.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('blog:home')
