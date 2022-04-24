from django import template

from women.models import *

register = template.Library()

@register.simple_tag(name='get_cats')  # Превращаем функцию в простой тег.
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=''):
    cats = Category.objects.all()
    return {'cats': cats,
            'cat_selected': cat_selected,
            }
