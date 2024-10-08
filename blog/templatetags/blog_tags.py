from django import template
from ..models import *
from markdown import markdown
from django.utils.safestring import mark_safe
import jdatetime

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
def tags_list(count=0, ref=None):
    if ref:
        return {'tags': Tag.objects.filter(articles=ref)}
    if count:
        return {'tags': Tag.objects.all()[:count]}
    return {'tags': Tag.objects.all()}


@register.simple_tag()
def last_articles(id, count=2):
    articles = Article.objects.all().exclude(id=id).order_by('-update_date')[:count]
    return articles


PERSIAN_MONTHS = [
    'فروردین', 'اردیبهشت', 'خرداد', 'تیر',
    'مرداد', 'شهریور', 'مهر', 'آبان',
    'آذر', 'دی', 'بهمن', 'اسفند'
]


@register.filter(name='jalali_date')
def jalali_date(value):
    if isinstance(value, (jdatetime.datetime, jdatetime.date)):
        day = value.day
        month = PERSIAN_MONTHS[value.month - 1]
        year = value.year
        return f'{day} {month} {year}'
    return value
