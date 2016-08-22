from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MailboxAngular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^messages/', 'ngmail.views.messages'),
    url(r'^user/([0-9]+)/edit/', 'ngmail.views.edit_user'),
    url(r'^users/', 'ngmail.views.users'),
    url(r'^admin/', include(admin.site.urls)),
)
