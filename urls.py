#
# LazyCook
# Copyright (c) 2011 Sporetree.com
#
from django.conf.urls.defaults import *
from lazycook.views import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', home),
    (r'^admin/', include(admin.site.urls)),
)
