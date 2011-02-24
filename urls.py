from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lazycook/', include('lazycook.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
