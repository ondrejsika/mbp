# django
from django import template


register = template.Library()


@register.filter
def ymdhm(variable):
    return variable.strftime('%Y-%m-%d %H:%M')
