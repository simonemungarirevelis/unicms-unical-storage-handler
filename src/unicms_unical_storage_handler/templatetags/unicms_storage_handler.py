import logging

from django import template
from django.conf import settings

from cms.contexts.models import WebSite

from .. settings import ALLOWED_UNICMS_SITES


logger = logging.getLogger(__name__)
register = template.Library()


ALLOWED_UNICMS_SITES = getattr(settings, 'ALLOWED_UNICMS_SITES',
                               ALLOWED_UNICMS_SITES)

@register.simple_tag
def clean_url(url):
    if url.find('?'): url = url.split('?')[0]
    if url[-1] == '/': return url[:-1]
    return url


@register.simple_tag
def get_cdsid_from_url(url):
    if url.find('?'): url = url.split('?')[0]
    pieces = url.split('/')
    return list(filter(None, pieces))[-1]


@register.simple_tag
def get_allowed_website(host):
    domain_params = host.split(":")
    domain = domain_params[0]
    port = domain_params[1] if len(domain_params)==2 else None
    websites = []
    websites = WebSite.objects.filter(pk__in=ALLOWED_UNICMS_SITES,
                                      is_active=True)
    current = websites.filter(domain=domain).first()
    active = current or websites.first()
    if port:
        return f'{active.domain}:{port}'
    return f'{active.domain}'


@register.simple_tag
def get_father_from_url(url):
    import re
    father = re.match('.*father=(.*)', url)
    return None if father is None else father.group(1)
