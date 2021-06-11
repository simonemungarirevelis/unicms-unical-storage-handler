import logging

from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# list of website pks allowed to display the pages
ALLOWED_UNICMS_SITES = [2]

# base path
CMS_STORAGE_BASE_PATH = 'storage/'

# as documentation reference or default
CMS_STORAGE_CDS_VIEW_PREFIX_PATH = f'{CMS_STORAGE_BASE_PATH}cds'
CMS_STORAGE_CDSLIST_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})(/)?$' # noqa
CMS_STORAGE_CDSINFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_CDS_VIEW_PREFIX_PATH})/(?P<code>[a-z0-9\-]*)(/)?$' # noqa

CMS_STORAGE_STUDIACTIVITYINFO_VIEW_PREFIX_PATH = f'{CMS_STORAGE_BASE_PATH}/studyactivityinfo'
CMS_STORAGE_STUDIACTIVITYINFO_URL_VIEW_REGEXP = f'^(?P<webpath>[\/a-zA-Z0-9\.\-\_]*)({CMS_STORAGE_STUDIACTIVITYINFO_VIEW_PREFIX_PATH})(?P<code>[a-z0-9\-]*)(/)?' # noqa

CMS_STORAGE_HANDLERS_PATHS = [CMS_STORAGE_CDSLIST_URL_VIEW_REGEXP,
                              CMS_STORAGE_CDSINFO_URL_VIEW_REGEXP,
                              CMS_STORAGE_STUDIACTIVITYINFO_URL_VIEW_REGEXP]

CMS_STORAGE_APP_REGEXP_URLPATHS = {
    # 'cms_storage.handlers.StudyActivityInfoViewHandler' : CMS_STORAGE_STUDIACTIVITYINFO_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSListViewHandler' : CMS_STORAGE_CDSLIST_URL_VIEW_REGEXP,
    'unicms_unical_storage_handler.handlers.CdSInfoViewHandler' : CMS_STORAGE_CDSINFO_URL_VIEW_REGEXP,
}

# cms_storage APIs (ref: https://storage.unical.it)
CMS_STORAGE_BASE_API = 'https://storage.portale.unical.it/api/ricerca/'

CMS_STORAGE_CDS_API = f'{CMS_STORAGE_BASE_API}cds/'
CMS_STORAGE_STUDIACTIVITYINFO_API = f'{CMS_STORAGE_BASE_API}studiactivityinfo/'

# labels (for breadcrumbs and page title)
CMS_STORAGE_ROOT_LABEL = _("Data storage")
CMS_STORAGE_CDSLIST_LABEL = _("Corsi di studio")
