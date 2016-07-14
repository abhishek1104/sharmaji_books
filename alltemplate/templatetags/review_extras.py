from django import template
from django.template.defaultfilters import stringfilter
import datetime

register=template.Library()


@register.filter(is_safe=True) #is_safe means if safe string is passed then result would be save otherwise auto escape!
@stringfilter
def cutwaoo(value,arg):
    return value.replace(arg,'')


@register.assignment_tag
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)