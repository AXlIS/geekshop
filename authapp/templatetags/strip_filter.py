from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def strip_filter(value):
    value = value.count('success')
    return int(value)