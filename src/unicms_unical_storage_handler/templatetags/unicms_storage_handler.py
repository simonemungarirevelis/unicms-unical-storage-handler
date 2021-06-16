import logging
import random
import string

from django import template


logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def random_id():
    # printing lowercase
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

@register.simple_tag
def clean_url(url):
    return url[:url.find('?')]

@register.simple_tag
def get_cdsid_from_url(url):
    cleaned = url[:url.find('?')]
    pieces = cleaned.split('/')
    return list(filter(None, pieces))[-1]
