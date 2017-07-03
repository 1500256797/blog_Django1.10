import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register =template.Library()#自定义filter时必须添上

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown2.markdown(value,
                                        extensions=[
                                            'markdown.extensions.fenced_code',
                                            'markdown.extensions.codehilite'
                                        ],
                                        safe_mode=True,
                                        nable_attribute=False))