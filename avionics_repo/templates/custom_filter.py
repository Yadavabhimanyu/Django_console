from django import template

register = template.Library()


@register.filter(name='time_format_change')
def time_format_change(input_time):
    return input_time.strftime("%I:%M %p")