from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


# Admin Settings
admin.site.site_header = "관리자 페이지"  # Django administration
admin.site.site_title = "관리자"
admin.site.index_title = "관리자 메인페이지"


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', include("ipify.urls.api", namespace="api")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
