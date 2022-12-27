from django import template
from django.utils.safestring import mark_safe
import markdown

from service.models import Settings, Service

register = template.Library()

@register.filter(name='markdown')
def makrdown_format(text):
	return mark_safe(markdown.markdown(text))

@register.simple_tag
def get_setting(key):
	return getattr(Settings.load(), key, None)

@register.simple_tag
def get_services():
	return Service.objects.all()