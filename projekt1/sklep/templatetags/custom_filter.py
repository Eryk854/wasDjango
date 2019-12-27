from django import template

register = template.Library()


@register.filter(name="is_numeric")
def numeric(value):
    return isinstance(value,float)


@register.filter(name="percentage")
def percentage(value):
    return str(value*100) + "%"


@register.filter(name="value")
def value(value, arg):
    return round(value - value*arg,2)