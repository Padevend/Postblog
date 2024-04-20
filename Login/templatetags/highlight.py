from django import template
from django.utils.safestring  import mark_safe
from django.template.defaultfilters import escape
import highlights

register = template.Library()
@register.filter(name='highlight')
def highlight(value, language):
    # return mark_safe(highlights.hi)
    pass