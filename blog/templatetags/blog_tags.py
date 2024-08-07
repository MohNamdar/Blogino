from django import template
from ..models import Article
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
