import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def md_convert(value):
    return md.markdown(value, extensions=['fenced_code'])
    