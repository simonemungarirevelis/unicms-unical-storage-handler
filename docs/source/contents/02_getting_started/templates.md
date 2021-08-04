Templates
---------

Templates are managed as atomic, inheritable and composable elements,
which can also be used in uniCMS to create independent
[blocks](https://unicms.readthedocs.io/en/latest/contents/usage.html#page-blocks)
to be inserted in its pages.

Every single template is a combination of ***HTML***, ***Django tags*** and ***Vue.js***.
This approach is extremely flexible.

#### Bases

| File | Description |
| -----|-------------|
| **unical_storage_list.html** | Base template inherited from every list view. Provides pagination, base search and base API calling methods |

#### Blocks

All blocks templates accept the same context parameters.

| Name | Required | Type | Description |
| -----|----------|------|-------------|
| **url** | yes | String | API source URL |
| **uid** | no | String | Manual unique id for Vue.js component and HTML elements id (if not present is ramdomly generated)|

| File | Description | API source | Extra context params |
| -----|-------------|------------|--------------|
| **unical_storage_addressbook.html** | Addressbook list | /api/ricerca/addressbook/ | structure_id (not required): structure id to populate filter with only its childs |
| **unical_storage_addressbook_info.html** | Addressbook single item | /api/ricerca/addressbook/{personaleid}/ | - |
| **unical_storage_addressbook_without_structure_filter.html** | Addressbook list without search filters | /api/ricerca/addressbook/ | - |
| **unical_storage_cdsinfo.html** | Single study course detail | /api/ricerca/cds/{cdsid}/ | - |
| **unical_storage_cdslist.html** | Study courses list | /api/ricerca/cds/ | - |
| **unical_storage_cdslist_without_course_types.html** | Study courses list without coursetype search filter | /api/ricerca/cds/ | - |
| **unical_storage_cdslist_without_filters.html** | Study courses list without search filters | /api/ricerca/cds/ | - |
| **unical_storage_cdsstudyplans.html** | Study course's studyplans list | api/ricerca/cds/{cdsid}/studyplans/ | - |
