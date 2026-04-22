from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path
from .views.html_export_site import html_export_site
from .views.html_export_object import html_export_object
from .views.html_export_feature import html_export_feature
from .views.html_export_collection import html_export_collection
from .views.html_export_oral_history import html_export_oral_history
from .views.html_export_digital_asset import html_export_digital_asset


urlpatterns = [
    re_path(r"^html_export_site$", html_export_site, name="html_export_site"),
    re_path(r"^html_export_object$", html_export_object, name="html_export_object"),
    re_path(r"^html_export_feature$", html_export_feature, name="html_export_feature"),
    re_path(r"^html_export_collection$", html_export_collection, name="html_export_collection"),
    re_path(r"^html_export_oral_history$", html_export_oral_history, name="html_export_oral_history"),
    re_path(r"^html_export_digital_asset$", html_export_digital_asset, name="html_export_digital_asset"),
]

# Ensure Arches core urls are superseded by project-level urls
urlpatterns.append(path("", include("arches.urls")))

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
