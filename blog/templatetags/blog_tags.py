from django import template
from ..models import *
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='markdown')
def to_markdown(text):
    return mark_safe(markdown(text))


@register.inclusion_tag('partials/category_list.html')
def category_list():
    choices = Article.Category.choices
    return {"categories": choices}


@register.simple_tag()
def article_counter(category=''):
    if category:
        return Article.objects.filter(category=category[0]).count()
    return Article.objects.all().count()


@register.inclusion_tag('partials/tags_list.html')
def tags_list(count=0):
    if count:
        return {'tags': Tag.objects.all()[:count]}
    return {'tags': Tag.objects.all()}


@register.simple_tag()
def last_articles(count=3):
    articles = Article.objects.all().order_by('-update_date')[:count]
    return articles
