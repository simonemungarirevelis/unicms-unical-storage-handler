from django.conf import settings
from django.http import (HttpResponse,
                         Http404)
from django.template import Template, Context
from django.utils.translation import gettext_lazy as _

from cms.contexts.handlers import BaseContentHandler
from cms.contexts.models import WebPath
from cms.contexts.utils import contextualize_template, sanitize_path
from cms.pages.models import Page

from . settings import *


class CdSListInfoViewHandler(BaseContentHandler):
    template = "storage_cdslist.html"

    def __init__(self, **kwargs):
        super(CdSListInfoViewHandler, self).__init__(**kwargs)
        self.match_dict = self.match.groupdict()
        self.webpath = WebPath.objects.filter(site=self.website,
                                              parent=None,
                                              is_active=True)\
                                      .first()
        self.code = self.match_dict.get('code', '')

        if self.webpath.site.pk not in settings.ALLOWED_UNICMS_SITES:
            raise Http404('Website not allowed to show this webpath')

        if not self.webpath or self.match_dict.get('webpath', '/') != self.webpath.fullpath: # pragma: no cover
            raise Http404('Unknown WebPath')

        self.page = Page.objects.filter(is_active=True,
                                        webpath=self.webpath).first()

    def as_view(self):
        # if not self.pub_context: return Http404()

        # i18n
        # lang = getattr(self.request, 'LANGUAGE_CODE', None)
        # if lang:
            # self.pub_context.publication.translate_as(lang=lang)

        data = {'request': self.request,
                'webpath': self.webpath,
                'website': self.website,
                'page': self.page,
                'path': self.match_dict.get('webpath', '/'),
                'handler': self,
                'url': f'{settings.CMS_STORAGE_CDSINFO_API}/{self.code}/'
        }

        ext_template_sources = contextualize_template(self.template,
                                                      self.page)
        template = Template(ext_template_sources)
        context = Context(data)
        return HttpResponse(template.render(context), status=200)

    @property
    def parent_path_prefix(self):
        return ''
        return getattr(settings, 'CMS_PUBLICATION_LIST_PREFIX_PATH',
                       CMS_PUBLICATION_LIST_PREFIX_PATH)

    @property
    def parent_url(self):
        url = f'{self.webpath.get_full_path()}/{self.parent_path_prefix}/'
        return sanitize_path(url)

    @property
    def breadcrumbs(self):
        # leaf = (self.pub_context.url, getattr(self.pub_context.publication, 'title'))
        leaf = ('#', 'ahahh')
        parent = (self.parent_url, _('News'))
        return (parent, leaf)
