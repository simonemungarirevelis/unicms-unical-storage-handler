Setup
-----

To install ***unicms_unical_storage_handler*** follow these easy steps:

````
pip install git+https://github.com/UniversitaDellaCalabria/unicms-unical-storage-handler.git
````

In your uniCMS ```settingslocal.py``` file, add app in your ```INSTALLED_APPS```

````
INSTALLED_APPS = [
    ...

    unicms_unical_storage_handler,
]
````

and set new handler

````
# UNICAL STORAGE HANDLER
if "unicms_unical_storage_handler" in INSTALLED_APPS:

    from unicms_unical_storage_handler.settings import *

    CMS_HANDLERS_PATHS.extend(CMS_STORAGE_HANDLERS_PATHS)
    CMS_APP_REGEXP_URLPATHS.update(CMS_STORAGE_APP_REGEXP_URLPATHS)

    # Set uniCMS websites pk list enabled to manage the new url
    # if different from default [1]
    ALLOWED_UNICMS_SITES = [2]
# END UNICAL STORAGE HANDLER
````

Finally, collect new templates

````
./manage.py unicms_collect_templates
````
