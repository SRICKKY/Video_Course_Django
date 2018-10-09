# Central URL file

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls',namespace='courses')),
    path('memberships/', include('memberships.urls', namespace='memberships')),
    path('account/', include('account.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)


# Make sure DEBUG=False in setting.py
# Cutom Error Page

handler404 = 'courses.views.my_custom_page_not_found_view'
handler500 = 'courses.views.my_custom_error_view'
handler403 = 'courses.views.my_custom_permission_denied_view'
handler400 = 'courses.views.my_custom_bad_request_view'


# Debug Toolbar

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
