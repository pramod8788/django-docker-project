from django import template
from ecommerce import models

register = template.Library()

@register.filter
def to_model_name(value):
    return value.__class__.__name__


@register.simple_tag
def cat_names():
    categories = models.Category.objects.all().order_by('category_name')
    return categories
