from django import template

register = template.Library()


# @register.filter(name='formatchange')
# def low(value):
#     return value.lower()